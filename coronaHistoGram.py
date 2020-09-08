import pandas as pd
import matplotlib.pyplot as plt

#data = pd.read_csv("coronaBD_Dhaka.csv", sep=',')
li = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000]
data = [82387,4700 ,5115 ,2580 ,1402 ,1258 ,6509 ,3277 ,2142 ,2789 ,6593 ,2762 ,1570 ,2387]
#plt.hist(data)
#plt.hist(data,bins=5)
#plt.show()
# plt.clf() #-> cleaning up plot

plt.hist(data,bins=35)
plt.show()

#plt.plot(li,data)
#plt.show()
print(data)

plt.scatter(li,data)
#plt.xscale('log') # logarithmic scale
#plt.show()

# =================== Basic scatter plot, log scale ===================

plt.scatter(li,data)
plt.xscale("log")
# string
xlab = 'city of dhaka'
ylab = 'list'
title = 'corona virus dhaka city'
# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
# add title
plt.title(title)
#plt.show()
# =================== Basic scatter plot, log scale ===================

# =================== definition of tick_val and dick_lab ===================
tick_val = [1000,2000,5000]
tick_lab = ['1k','2k','5k']

# adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)
# plt.show()
# =================== definition of tick_val and dick_lab ========== (end) =========

import numpy as np
np_data = np.array(data)
np_data *= 2

# update: set s argument to np_data
plt.scatter(li,data,s=np_data)
plt.show()

# coloring
# specify c (color) and alpha inside the scatter
'''col = ['red', 'green', 'blue', 'blue', 'yellow', 'black', 'green', 'red', 'red',
       'green', 'blue', 'yellow', 'green', 'blue', 'yellow', 'green', 'blue', 'blue',
       'red', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'yellow', 'blue', 'blue',
       'blue', 'yellow', 'blue', 'green', 'yellow', 'green', 'green', 'blue', 'yellow',
       'yellow', 'blue', 'yellow', 'blue', 'blue', 'blue', 'green', 'green', 'blue', 'blue',
       'green', 'blue', 'green', 'yellow', 'blue', 'blue', 'yellow', 'yellow', 'red', 'green',
       'green', 'red', 'red', 'red', 'red', 'green', 'red', 'green', 'yellow', 'red', 'red',
       'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red',
       'blue', 'blue', 'blue', 'yellow', 'red', 'green', 'blue', 'blue', 'red', 'blue', 'red',
       'green', 'black', 'yellow', 'blue', 'blue', 'green', 'red', 'red', 'yellow', 'yellow',
       'yellow', 'red', 'green', 'green', 'yellow', 'blue', 'green', 'blue', 'blue', 'red',
       'blue', 'green', 'blue', 'red', 'green', 'green', 'blue', 'blue', 'green', 'red',
       'blue', 'blue', 'green', 'green', 'red', 'red', 'blue', 'red', 'blue', 'yellow',
       'blue', 'green', 'blue', 'green', 'yellow', 'yellow', 'yellow', 'red', 'red', 'red',
       'blue', 'blue']
'''
col = ['red', 'green', 'blue', 'blue', 'yellow', 'black', 'green',
       'red', 'red','green', 'blue', 'yellow', 'green', 'blue']
plt.scatter(li,data,np_data,c=col,alpha=0.8)
plt.xscale("log")
# string
xlab = 'Dhaka Division'
ylab = 'Days'
title = 'corona virus dhaka division'
# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
# add title
plt.title(title)
# definition of tick_val and dick_lab
tick_val = [82387,4700 ,5115 ,2580 ,1402 ,1258 ,6509 ,3277 ,2142 ,2789 ,6593 ,2762 ,1570 ,2387]
tick_lab = ['Dhaka City','Dhaka (District)','Gazipur' ,'Kishoreganj','Madaripur' ,'Manikganj' ,'Narayanganj', 'Munshigonj' ,
            'Narshingdi' ,'Rajbari' ,'Faridpur' ,'Tangail' ,'Shariatpur', 'Gopalganj']

# adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)
# Additional Customization
#plt.text(14,14,'What is this!!')
#plt.text(10,10,'hehehehe')
# Add grid() call
#plt.grid(True)
plt.show()
