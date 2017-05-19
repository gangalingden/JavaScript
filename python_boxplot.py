import matplotlib
import matplotlib.pyplot as plt
import numpy 

values = []
with open('winequality-red.csv') as f:
	next(f)
	for line in f:
		acidity= line.split(';')[0]
		values.append(float(acidity))

plt.boxplot(values)
plt.show()