import formatData
# requests module required to make API calls
import requests

def post(currency):
    # IFTTT trigger event
    event = 'bitcoin_price_update'
    # IFTTT key
    key = 'czUTpArVbl_O6MBktVCvuG'
    # IFTTT webhook url
    postUrl = f'https://maker.ifttt.com/trigger/{event}/with/key/{key}'
    # acquired data to be passed to webhook
    data = formatData.getFormattedData(currency)
    # making POST request to IFTTT webhook
    #-----requests.post(postUrl, json= {'value1':data})
    return data