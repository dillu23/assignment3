'''
Created on Nov 16, 2012

@author: hp
'''
from test1.models import edgedata
correlation=[[]]*100
p=edgedata.objects.filter(LABEL=-23)
for i in p:
    cluster= int(i.CLUSTERSOURCE)
    target= int(i.CLUSTERTARGET)
    if target>=len(correlation[cluster]):
        correlation[i.CLUSTERSOURCE].append(1)
    else:
        correlation[i.CLUSTERSOURCE][target]=int(correlation[i.CLUSTERSOURCE][target]+1 )

sum1=0
for i in range(1,59):
    for j in range(1,59):
        print correlation[i][j]
        sum1=sum1+correlation[i][j]
        
print sum1