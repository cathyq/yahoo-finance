# convert our RDD of strings to numeric data so we can compute stats and remove the outliers.



distanceNumerics = distance.map(lambda string: float(string))
stats = distanceNumerics.stats()
stddev = stats.stddev()
mean = stats.mean()
reasonableDistances = distanceNumerics.filter(
	lambda x: math.fabs(x-mean) > 2 * stddev)
print reasonableDistances.collect()