# https://github.com/aghasemi/streamlit_js_eval/tree/master
# https://api-ninjas.com/api/salestax

import streamlit as st
from streamlit_js_eval import get_geolocation
import geopy
import requests
import json


# custom error class
class TaxError(Exception):
    pass


def get_tax_rate():
    tax_rate = 0
    zip_code = 0
    
    loc = get_geolocation()
    print(loc)
    if loc:
        # extract coordinates
        lat = loc['coords']['latitude']
        lon = loc['coords']['longitude']

        # extract zip code
        geolocator = geopy.Nominatim(user_agent='gold')
        location = geolocator.reverse((lat, lon))
        zip_code = location.raw['address']['postcode']

        # extarct the tax rates
        api_url = 'https://api.api-ninjas.com/v1/salestax?zip_code={}'.format(zip_code)
        response = requests.get(api_url, headers={'X-Api-Key': 'sGhg355U0zFi6kLq5oJ6dw==cmIKqhUVUGtNjJGJ'})
        if response.status_code == requests.codes.ok:
            json_string = response.text
            data = json.loads(json_string)
            tax_rate = data[0]["total_rate"]
        else:
            return TaxError("tax error")
    return zip_code, tax_rate
