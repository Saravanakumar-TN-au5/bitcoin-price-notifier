# time module for makingAPI call with intervals
# datetime module for adding date and time to data
import time, datetime
import makeAPICall

# gets price data and populate it with date and time
def getFormattedData(currency):
    out = ''
    for i in range(5):
        # gets current datetime in preferred format
        dt = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        # gets price data making API call
        priceData = makeAPICall.get_data(currency)
        # formatted data
        out += f'{dt}: {priceData}\n'
        # setting interval in seconds
        time.sleep(1)
    return out