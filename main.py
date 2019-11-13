import csv
import pdb
import math
import matplotlib.pyplot as plt
import numpy as np


sum = [0] * 100
j = 0
plt_index = np.arange(0,100,1)
with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        #print(row[1]) --> i want see if previous codes work well.
        for i in range(0,len(row)):
            sum[j] += pow(int(row[i]),2)
            #pdb.set_trace() --> breakpoint for error handling. 
            
        sum[j] = int(math.sqrt(sum[j]))
             
        j += 1
print(sum)
plt.plot(plt_index,sum)

plt.show()

