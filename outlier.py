import math
from pyspark import SparkContext

sc = SparkContext(appName = "yahoo-finance")

companies = ["ibm", "facebook", "nyt", "linkedin", "yahoo"]

for company in companies:
    data = sc.textFile("data/{0}.txt".format(company))
    data = data.map(lambda line: float(line))
    stats = data.stats()
    stddev = stats.stdev()
    mean = stats.mean()

    outliers = data.filter(lambda x: math.fabs(x-mean) >= 2*stddev)
    outliers.saveAsTextFile("{0}_outliers".format(company))
