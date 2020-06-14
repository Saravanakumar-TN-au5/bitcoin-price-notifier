# bitcoin-price-notifier
A python app for alerts and updates on bitcoin price

## Modules
**makeAPICall :**
   Responsible for getting price data, given the currency_code. It returns the data as a string with currency symbol and price e.g *$ 10230*. Data is retrieved from **blockchain** API by GET request.
				   
**formatData :**
This module is responsible for formatting and populating the acquired data from makeAPICall module with date and time. The timezone is of IST. It returns a string with 5 sets of price data e.g *14.06.2020 15:12 : $ 10230*.
		
**postToIFTTT :**
It makes a POST request to IFTTT webhook with formatted data, which in turn triggers an event. An IFTTT applet is created with an webhook as *this* and Telegram message service as *that*. It is implemented in a way such that whenever a POST request is made to the webhook, a message will be received in Telegram with formatted data.
			
**bitcoinNotifier :**
This is the main module which makes use of all other modules, to facilitate either getting continuous updates on bitcoin price or getting alerts when price reaches certain given value.

## Parameters
Either we can get updates or alerts when the bitcoin price reaches certain value. The parameters are given in the following manner.

For updates:
		
		py bitcoinNotifier.py update INR

For alerts:

				
		py bitcoinNotifier.py alert below INR 710000
		py bitcoinNotifier.py alert above USD 11000

## IFTTT Applets
Two applets are created one for updates on price and the other for getting alerts when the price reaches certain value. Above scripts are made available as an API using Flask framework and hosted on [pythonanywhere.com].

**API Endpoints**
The query parameters are similar to the parameters defined above.
					
	http://tns1695.pythonanywhere.com/get-price?currency=INR
	http://tns1695.pythonanywhere.com/get-prices?currency=INR
	http://tns1695.pythonanywhere.com/alert?cond=below&currency=INR&price=716100
**For Updates :**
	Two services are created 
 1. IF *telegram text to @IFTTT bot* THEN *web request to **get-prices** endpoint* which in turn will make a POST request to the next service's webhook.
 2. IF *web request* with webhook THEN *telegram text to the t.me/bitcoin_price_notifier* channel.
 
If **Update** text is sent to the Telegram IFTTT bot, then a text with price data will be received to the specified channel.

**For Alerts:**
Two services are created, similar to updates

 1. IF *google assistant query with **alert $ #***  THEN *web request to **alert** endpoint* which in turn will make a POST request to the next service's webhook.
 2. IF *web request* with webhook THEN *telegram text to the specified channel*.

where $ can be *above* or *below* and # can be any price value to set the alert for.
