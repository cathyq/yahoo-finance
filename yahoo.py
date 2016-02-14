import time
from yahoo_finance import Share

# Collect 30 mins of Finance data on 5 companies, one value per minute
nyt = Share('NYT')
ibm = Share('IBM')
google = Share('GOOG')
facebook = Share('FB')
linkedin = Share('LNKD')

for minute in range(30):
	print "%s minutes" % minute
	nyt.refresh()
	print "The New York Times' stock price is $%s" % nyt.get_price()
	ibm.refresh()
	print "IBM's stock price is $%s" % ibm.get_price()
	google.refresh()
	print "Google's stock price is $%s" % google.get_price()
	facebook.refresh()
	print "Facebook's stock price is $%s" % facebook.get_price()
	linkedin.refresh()
	print "Linkedin's stock price is $%s" % linkedin.get_price()
	time.sleep(60)

