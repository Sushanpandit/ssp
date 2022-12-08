import csv
import os
import collections
from collections import Counter
filename = 'earthquakePast.csv'

lats,lons = [], []
epicentre,magnitudes = [],[]
timestrings = []

l=[]
#with statement automatically closes the file again when the block end
#next(reader) # Move to next Row, Ignore the header in this case.
'''
    fp=open('','r')
    ......
    ......
    fp.close()
'''

#'c:\python37\test.txt'

#with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename) as f:

with open(filename) as f:  #file handler
    reader = csv.reader(f)
    #print(reader)
    #print(type(reader))
    for row in reader:
        print(row[-1])
        print(1.append(row[2])
print(len(1))
print(counter(1))
