import sys
from postToIFTTT import post
from makeAPICall import get_data

def main():
    # for getting price updates
    if sys.argv[1] == 'update':
        currency_code = sys.argv[2]
        while True:
            print(post(currency_code))
    # for price alerts
    elif sys.argv[1] == 'alert':
        condition = sys.argv[2]
        currency_code = sys.argv[3]
        check_price = sys.argv[4]
        if condition == 'below':
            while True:
                priceStr = get_data(currency_code)
                price = float(get_data(currency_code)[2:])
                if price < float(check_price):
                    print (f'Alert ! Bitcoin price reached below {check_price} \n Current price: {priceStr}')
                    return
                else:
                    print (get_data(currency_code))
        elif condition == 'above':
            while True:
                priceStr = get_data(currency_code)
                price = float(get_data(currency_code)[2:])
                if price > float(check_price):
                    print (f'Alert ! Bitcoin price reached above {check_price} \n Current price: {priceStr}')
                    return
                else:
                    print (get_data(currency_code))


main()