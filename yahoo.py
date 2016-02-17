import time
from yahoo_finance import Share

# Collect 30 mins of Finance data on 5 companies, one value per minute

for minute in range(30):
	nyt = Share('NYT')
	ibm = Share('IBM')
	google = Share('GOOG')
	facebook = Share('FB')
	linkedin = Share('LNKD')
	
	print "%s minutes" % minute

	print nyt.get_trade_datetime()
	print "The New York Times' stock price is $%s" % nyt.get_price()

	print ibm.get_trade_datetime()
	print "IBM's stock price is $%s" % ibm.get_price()

	print google.get_trade_datetime()
	print "Google's stock price is $%s" % google.get_price()

	print facebook.get_trade_datetime()
	print "Facebook's stock price is $%s" % facebook.get_price()

	print linkedin.get_trade_datetime()
	print "Linkedin's stock price is $%s" % linkedin.get_price()

	
	nyt.refresh();
	ibm.refresh();
	google.refresh();
	facebook.refresh();
	linkedin.refresh();
	
	time.sleep(60)

