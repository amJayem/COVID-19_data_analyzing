#li = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000]#,14000]
li = [1258,1402,1570,2142,2387,2580,2762,2789,3277,4700,5115,6509,6593]
data = [1258,1402,1570,2142,2387,2580,2762,2789,3277,4700,5115,6509,6593]#,82387] #82387
col = ['red', 'green', 'yellow', 'green', 'yellow', 'black', 'green',
       'yellow', 'red','green', 'red', 'yellow', 'green']#, 'blue']



tick_value = [82387,4700 ,5115 ,2580 ,1402 ,1258 ,6509 ,3277 ,2142 ,2789 ,6593 ,2762 ,1570 ,2387]
tick_label = ['Dhaka City','Dhaka (District)','Gazipur' ,'Kishoreganj','Madaripur' ,'Manikganj' ,'Narayanganj', 'Munshigonj' ,
            'Narshingdi' ,'Rajbari' ,'Faridpur' ,'Tangail' ,'Shariatpur', 'Gopalganj']

# ===================== ploting =========== (start) ==========
import matplotlib.pyplot as p
p.plot(data,li)
p.title("plotting")
p.xlabel('Cases')
p.ylabel('')
p.title('Title: Dhaka Division case result (IEDCR [6.9.2020])')

#p.show()
p.clf()
# ===================== ploting =========== (end) ==========

# ===================== scatter ploting =========== (start) ==========
p.scatter(data,li)
p.xscale('log')
p.title("scatter plotting with LOG")
p.xlabel('Cases')
p.ylabel('District wise case number')
p.title('Title: Dhaka Division case result (IEDCR [6.9.2020])')

p.text(1258,1200,'1.Manikganj [1,258]')
p.text(1402,1409,'2.Madaripur [1,402]')
p.text(1570,1574,'3.Shariatpur [1,570]')
p.text(2146,2056,'4.Narshingdi [2,142]')
p.text(2414,2322,'5.Gopalganj [2,387]')
p.text(2604,2540,'6.Kishoreganj [2,580]')
p.text(2766,2688,'7.Tangail [2,762]')
p.text(2806,2805,"8.Rajbari [2,789]")
p.text(3287,3273,'9.Munshigonj [3,277]')
p.text(4700,4710,'10.Dhaka City [4,700]')
p.text(5127,5106,'11.Gazipur [5,115]')
p.text(6478,6448,'12.Narayanganj [6,509]')
p.text(6646,6628,'13.Faridpur [6,593]')

p.show()
p.clf()
# ===================== scatter ploting =========== (end) ==========

# ===================== Building histogram =========== (start) ==========
p.hist(data,bins=20)
p.title("histogram generating")
p.xlabel('Cases')
p.ylabel('District wise case number')
p.title('Title: Dhaka Division case result (IEDCR [6.9.2020])')

p.show()
p.clf()
# ===================== Building histogram =========== (end) ==========

# ===================== Labeling =========== (start) ==========
xlab = 'Dhaka Division'
ylab = 'District wise case number'
title = '(labeling) corona virus dhaka division'
p.xlabel(xlab)
p.ylabel(ylab)
p.title(title)
#p.show()
p.clf()
# ===================== Labeling =========== (end) ==========

# ===================== Tick Value =========== (start) ==========
tick_value = [1258,1402,1570,2142,2387,2580,2762,2789,3277,4700,5115,6509,6593] # 82387]
tick_label = ['1.2k','1.4k','1.5k','2.1k','2.3k','2.5k','2.76k','2.78k','3.2k','4.7k','5.1k','6.50k','6.59k']#,'82.3k']
'''tick_label = ['Mkgnj','Mdripr','Sriatpr','Nshngd','Gpgnj','Kshrgnj','Tngl','Rjbri',
'Mnshignj','Dh(Dis)','Gzpr','Ngnj','Fridpr','Dhk_82387']'''

p.xticks(tick_value,tick_label)
#p.show()
# ===================== Tick Value =========== (end) ==========

# ===================== Sizing =========== (start) ==========
import numpy as n
n_data = n.array(data)
p.scatter(data,li,n_data*2)

xlab = 'Dhaka Division'

title = 'corona virus dhaka division (recent)'
p.xlabel(xlab)
p.ylabel('District wise case number')
p.title(title)
p.show()
p.clf()
# ===================== Sizing =========== (end) ==========

# ===================== Coloring =========== (start) ==========
p.scatter(data,li,n_data*2,c=col,alpha=1);p.xscale('log');p.xlabel(xlab);p.ylabel(ylab);p.title("coloring")
p.xticks(tick_value)#,tick_label)
# Additional
p.grid(True)

p.text(1258,1200,'1.Manikganj [1,258]')
p.text(1402,1409,'2.Madaripur [1,402]')
p.text(1570,1574,'3.Shariatpur [1,570]')
p.text(2146,2056,'4.Narshingdi [2,142]')
p.text(2414,2322,'5.Gopalganj [2,387]')
p.text(2604,2540,'6.Kishoreganj [2,580]')
p.text(2766,2688,'7.Tangail [2,762]')
p.text(2806,2805,"8.Rajbari [2,789]")
p.text(3287,3273,'9.Munshigonj [3,277]')
p.text(4700,4710,'10.Dhaka City [4,700]')
p.text(5127,5106,'11.Gazipur [5,115]')
p.text(6478,6448,'12.Narayanganj [6,509]')
p.text(6646,6628,'13.Faridpur [6,593]')

p.xlabel('')
p.ylabel('District wise case number')
p.title('Title: Dhaka Division case result (IEDCR [6.9.2020])')

p.show()
# ===================== Coloring =========== (end) ==========