# convert our RDD of strings to numeric data so we can compute stats and remove the outliers.

from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF, IDF
path = '/Users/cathyq/code/yahoo-finance/yahoo_output'
sc = SparkContext(appName = "yahoo-finance")

distance = sc.wholeTextFiles("data")
distanceNumerics = distance.map(lambda string: float(string))
stats = distanceNumerics.stats()
stddev = stats.stddev()
mean = stats.mean()
reasonableDistances = distanceNumerics.filter(
	lambda x: math.fabs(x-mean) > 2 * stddev)
print reasonableDistances.collect()
reasonableDistances.saveAsTextFile(path)