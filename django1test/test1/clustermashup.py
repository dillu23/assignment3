from test1.models import edgedata,clustertopicinter
from django.db.models import Count,Sum

edata=edgedata.objects.all()
clusters=clustertopicinter.objects.filter(day__gt=0)
count=clusters.count()

arr=[""]*count
i=0
for cluster in clusters:
    list1={}
    list1["day"]=8-cluster.day
    list1["cluster"]=cluster.clusterID
    list1["inter"]=cluster.inter
    list1["intra"]=cluster.intra
    list1["size"]=cluster.size
    list1["total"]=int(cluster.inter)+int(cluster.intra)
    thres=int(list1["inter"]/50)
    j=list1["day"]
    if j==1:
        t=edata.filter(SOURCE=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day8")).filter(d1__gt=thres).count()
        t1=edata.filter(TARGET=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day8")).filter(d1__gt=thres).count()
    if j==2:
        t=edata.filter(SOURCE=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day7")).filter(d1__gt=thres).count()
        t1=edata.filter(TARGET=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day7")).filter(d1__gt=thres).count()
    if j==3:
        t=edata.filter(SOURCE=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day6")).filter(d1__gt=thres).count()
        t1=edata.filter(TARGET=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day6")).filter(d1__gt=thres).count()
    if j==4:
        t=edata.filter(SOURCE=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day5")).filter(d1__gt=thres).count()
        t1=edata.filter(TARGET=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day5")).filter(d1__gt=thres).count()
    if j==5:
        t=edata.filter(SOURCE=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day4")).filter(d1__gt=thres).count()
        t1=edata.filter(TARGET=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day4")).filter(d1__gt=thres).count()    
    if j==6:
        t=edata.filter(SOURCE=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day3")).filter(d1__gt=thres).count()
        t1=edata.filter(TARGET=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day3")).filter(d1__gt=thres).count()    
    if j==7:
        t=edata.filter(SOURCE=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day2")).filter(d1__gt=thres).count()
        t1=edata.filter(TARGET=cluster.clusterID).values("TOPIC").annotate(d1=Sum("day2")).filter(d1__gt=thres).count()    
    list1["topics"]=int((t+t1)/2)
    arr[i]=list1
    i=i+1
    
print arr    