import time
from yahoo_finance import Share
import sys

# Collect 30 mins of Finance data on 5 companies, one value per minute

share = Share(sys.argv[1])

for i in range(30):
	share.refresh();
	print share.get_price()
	time.sleep(60)

