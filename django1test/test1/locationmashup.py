from test1.models import locationtopicinter,locationtopicdata
from django.db.models import Sum,Count
topics=locationtopicdata.objects.all()
locations=locationtopicinter.objects.filter(day__gt=0)
count=locations.count()

arr=[""]*count
j=0
for location in locations:
    list1={}
    list1["day"]=8-location.day
    list1["location"]=location.locationname
    list1["inter"]=location.inter
    list1["intra"]=location.intra
    list1["size"]=location.size
    list1["total"]=int(location.inter)+int(location.intra)
    thres=int(location.intra/50)
    i=list1["day"]
    t=0
    #print thres
    if i==1:
        t=topics.filter(LOCATION=location.locationname,day8__gt=0).count()
    if i==2:
        t=topics.filter(LOCATION=location.locationname,day7__gt=thres).count()
    if i==3:
        t=topics.filter(LOCATION=location.locationname,day6__gt=thres).count()
    if i==4:
        t=topics.filter(LOCATION=location.locationname,day5__gt=thres).count()
    if i==5:
        t=topics.filter(LOCATION=location.locationname,day4__gt=thres).count()
    if i==6:
        t=topics.filter(LOCATION=location.locationname,day3__gt=thres).count()
    if i==7:
        t=topics.filter(LOCATION=location.locationname,day2__gt=thres).count()
    list1["topics"]=t
    arr[j]=list1
    j=j+1
    
print arr