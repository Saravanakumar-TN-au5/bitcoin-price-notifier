# requests module required to make API calls
import requests

def get_data(currency_code):
    try:
        # GET call to get data from API
        response = requests.get('https://blockchain.info/ticker')
        # Check if API call is successfull
        if response.status_code == 200:
            # Resultant Response object converted to JSON format
            data = response.json()
        else:
            # Raise exception if API call is not successfull
            raise Exception('No data at this time')
        return f'{data[currency_code]["symbol"]} {data[currency_code]["last"]}'

    except Exception as error:
        return error