import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

def get_price():
    url = "https://www.kitco.com/"  # Replace with the actual URL
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    element = soup.find("span", class_="flex min-w-[140px] justify-end text-sm font-bold tablet:min-w-[155px] desktop:min-w-[55px] desktop:text-[11.5px]")

    text = element.text
    ounce_price = float(text.replace(",", ""))
    gram_price = ounce_price/31.103

    time_zone = pytz.timezone('America/New_York')
    current_time = datetime.now(time_zone).strftime("%I:%M %p")
    current_date = datetime.now(time_zone).strftime("%B %d, %Y")
    return round(ounce_price, 2), gram_price, current_time, current_date