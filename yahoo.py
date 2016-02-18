import time
from yahoo_finance import Share
import sys

# Collect 30 mins of Finance data on 5 companies, one value per minute

share = Share(sys.argv[1])

for i in range(30):
	share.refresh();
	print share.get_price()
	time.sleep(60)

# RUN SCRIPT IN PYTHON
# python yahoo.py LNKD> linkedin.txt
# python yahoo.py FB> facebook.txt
# python yahoo.py IBM> ibm.txt
# python yahoo.py YHOO> yahoo.txt
# python yahoo.py NYT> nyt.txt