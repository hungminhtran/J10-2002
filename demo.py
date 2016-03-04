'''Vab =! Vba
V: vocabulary frequency
Local: frequency of each word divided by the frequency of the number of words in the text
Global: log frequency of words obtained from a large corpus
new word: ignore
Vab: subtract

600 texts:
choosen random 2*500 pair, create vector and train

six-fold cross-validation
run 6 times
divided to 6 equal subsamples
1 for test
5 for train: 2*500, each set get random 100 pair
'''
#calculate the frequency of global word
from math import log10
import os
HARD_DOCS = 'hard_docs'
EZ_DOCS = 'ez_docs'
TEST_HARD_DOCS = 'test_hard_docs'
TEST_EZ_DOCS = 'test_ez_docs'

f = open('words_freq.txt', 'r')
globalSum = 0
globalVals = []
globalStrs = []

for line in f:
	temp = line.split('	')
	globalSum += int(temp[1])
	globalStrs.append(temp[0])
	globalVals.append(int(temp[1]))
f.close()
for i in range(0, len(globalVals)):
	globalVals[i] = -log10(float(globalVals[i])/globalSum)
#calculate the frequency of local word
hardWordfreq = [[]]
for root, dirs, files in os.walk(HARD_DOCS):
    for _f in range(0,len(files)):
    	f = open(HARD_DOCS + '/' + _file, 'r')
    	temp = f.read()
    	for i in range(0, len(globalStrs)):
			hardWordfreq[_f].append(temp.count(globalStrs[i]))
    	f.close()

ezWordfreq = [[]]
for root, dirs, files in os.walk(EZ_DOCS):
    for _f in range(0,len(files)):
    	f = open(EZ_DOCS + '/' + _file, 'r')
    	temp = f.read()
    	for i in range(0, len(globalStrs)):
			ezWordfreq[_f].append(temp.count(globalStrs[i]))
    	f.close()
X = []
Y = []
for ezDoc in ezWordfreq:
	for hardDoc in hardWordfreq:
		temp = ezDoc + hardDoc
		x.append(temp)
		Y.append(0)
		temp = hardDoc + ezDoc
		x.append(temp)
		Y.append(1)
from sklearn import svm
clf = svm.SVC()
clf.fit(X, Y)  