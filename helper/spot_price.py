import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
import json

# custom error class
class CustomError(Exception):
    pass

def get_price_v1():
    url = "https://online.kitco.com/"  # Ensure the URL is correct
    try:
        response = requests.get(url, timeout=100)  # Add timeout to handle slow responses
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        raise CustomError(f"Failed to fetch data from Kitco: {e}")

    soup = BeautifulSoup(response.content, "html.parser")

    # Try to find the price element, handle the case if it's not found
    element = soup.find("div", class_="data-blk col-xs-6 col-sm-3").find("span", class_="price")

    try:
        # Extract and convert the price to float
        text = element.text.strip()
        ounce_price = float(text.replace(",", ""))  
    except ValueError:
        raise CustomError("Failed to convert price to float")
    
    if len(text) <= 1:
        raise CustomError("Kitco.com is down")

    # Convert ounce price to gram price
    gram_price = round(ounce_price / 31.1035, 2)

    # Get the current time and date in the 'America/Chicago' timezone
    time_zone = pytz.timezone('America/Chicago')
    current_time = datetime.now(time_zone).strftime("%I:%M %p")
    current_date = datetime.now(time_zone).strftime("%B %d, %Y")

    return round(ounce_price, 2), gram_price, current_time, current_date


def get_price():
    url = "https://kdb-gw.prod.kitco.com/"
    
    # Get the timestamp
    current_datetime = datetime.now()
    current_timestamp = int(current_datetime.timestamp())                                                 

    headers = {
        "accept": "application/graphql-response+json, application/json",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "connection": "keep-alive",
        "content-type": "application/json",
        "origin": "https://www.kitco.com",
        "referer": "https://www.kitco.com/",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    data = {
        "query": """
        query MetalQuote($symbol: String!, $currency: String!, $timestamp: Int!) {
        GetMetalQuoteV3(symbol: $symbol, currency: $currency, timestamp: $timestamp) {
            ...MetalFragment
        }
        }
        fragment MetalFragment on Metal {
        ID
        symbol
        currency
        name
        results {
            ...MetalQuoteFragment
        }
        }
        fragment MetalQuoteFragment on Quote {
        ID
        ask
        bid
        change
        changePercentage
        close
        high
        low
        mid
        open
        originalTime
        timestamp
        unit
        }
        """,
        "variables": {
            "currency": "USD",
            "symbol": "AU",
            "timestamp": current_timestamp
        },
        "operationName": "MetalQuote"
    }

    # post request
    response = requests.post(url, headers=headers, json=data, verify=True)

    # extracting the ask price
    a = response.json()
    ounce_price = a['data']['GetMetalQuoteV3']['results'][0]['ask']

    # Convert ounce price to gram price
    gram_price = round(ounce_price / 31.1035, 2)

    # Get the current time and date in the 'America/Chicago' timezone
    time_zone = pytz.timezone('America/Chicago')
    current_time = datetime.now(time_zone).strftime("%I:%M %p")
    current_date = datetime.now(time_zone).strftime("%B %d, %Y")

    return round(ounce_price, 2), gram_price, current_time, current_date
