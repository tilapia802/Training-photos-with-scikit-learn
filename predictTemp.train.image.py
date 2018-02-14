#import csv
import numpy as np
from skimage import data, io, filters
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

f = open(input_file, 'rb')
#im = io.imread("data/22834875504_33e7c35a5a_resize.jpg")
#print im
X = []
Y = []
total_num = 0
count=0
for row in f:
	#if count % 2 == 0 and row[0]!='.':  #xxx.jpg
		#print row
		count = count + 1
		photo_path = "data_0105/sea/photo_new/photo_temp/" + row[:len(row)-1] 
		#print photo_path
		im = io.imread(photo_path)	
		#print im.shape
		if im.shape != (160, 240, 3):
			im = np.dstack((im, im, im))
		x = np.array(im)
		x = x.ravel()
		#if len(x) !=115200:
		#	print "oo"
		#x = [float(i) if i else 0 for i in x]
		#if count ==1:
			#print len(x)
		X.append(x)
		#print X
		total_num = total_num + 1 
		#elif count % 2 == 1 and row[0]=='.':  #.xxx
		#print row
		#print float(row[1:3])
		if row[0] == 't' and row[1] == '3': 
			Y.append(float(3000))
			print 3000
		elif row[0] == 't' and row[1] == '5':
			Y.append(float(5000))
			print 5000
		elif row[0] == 't' and row[1] == '1':
			Y.append(float(13000))
		elif row[0] == 't' and row[1] == '4':
			Y.append(float(40000))
		else:
			Y.append(float(8000))
			
	#else:
		
	
	#print row
	#count = count + 1	
#	row2 = row[0:3]
	#print row2
#	row2 = [float(i) if i else 0 for i in row2]
#	row2.append(float(row[6]) - (float(row[8]) if row[8] else 0))
#	row2.append(float(row[3]))
#	row2.append(float(row[37]))
#	row2.append(float(row[38]))
	#print row2
#	X.append(row2)
#	y.append(float(row[33]))
	#print float(row[25])

#print X
print "begin traning"
train_num = int(total_num*0.7)
#np.random.shuffle(X)
#train_num=200
#print X[:1]
#print Y[:1]
#from sklearn import preprocessing
#im = preprocessing.scale(im)

from sklearn.neural_network import MLPRegressor
clf = MLPRegressor(solver='lbfgs', hidden_layer_sizes=(100,100,100), max_iter=200)
print clf.fit(X[:train_num], Y[:train_num])

from sklearn.externals import joblib
joblib.dump(clf, output_file)

print clf.score(X[:train_num], Y[:train_num])

test_num = 0
accuracy = 0
for i in range(train_num, total_num, 1):
	dec = clf.predict([X[i]])
	test_num = test_num + 1

	accuracy = accuracy + abs(dec[0]-Y[i])/37000.0
	print dec[0], Y[i], abs(dec[0]-Y[i])/37000.0
accuracy = accuracy / (float)(test_num)
print accuracy

