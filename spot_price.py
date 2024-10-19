import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

# custom error class
class CustomError(Exception):
    pass

def get_price():
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