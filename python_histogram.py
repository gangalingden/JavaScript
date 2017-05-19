import matplotlib
import matplotlib.pyplot as plt
import numpy 

values = []
with open('winequality-red.csv') as f:
	next(f)
	for line in f:
		acidity= line.split(';')[1] # split given index attributes
		values.append(float(acidity))


#Struges; bin = 13.258 = log2(1600-1)+1
# Scott's bin  = 5
#Square-root bin; 40
#Standard-deviation : 1.741
#IQR = 2.1
#Freedman=35

plt.hist(values, bins=35, normed=True, color='red') 
plt.ylabel('Quality')
plt.xlabel('Fixed acidity')

plt.show()

#standard_deviation = numpy.std(values) # 1.74055180011

#print (standard_deviation)
# a,b = numpy.percentile(values,[75,25])
# ans = a-b
# print ans

