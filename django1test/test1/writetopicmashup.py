from test1.models import edgedata
from django.db.models import Count,Sum
from django.utils.safestring import SafeString

alltopics=edgedata.objects.all()
topics =edgedata.objects.values("TOPIC").annotate(d1=Sum("day8")).annotate(d2=Sum("day7")).annotate(d3=Sum("day6")).annotate(d4=Sum("day5")).annotate(d5=Sum("day4")).annotate(d6=Sum("day3")).annotate(d7=Sum("day2"))
count=topics.count()
arr=[""]*count*7
i=0;
for topic in topics:
    list1={}
    list1["day"]=1
    list1["topic"]=topic["TOPIC"].encode('latin-1')
    list1["total"]=topic["d1"]
    thres=int(list1["total"]/50)
    t=alltopics.filter(TOPIC=topic["TOPIC"]).values("SOURCE").annotate(sum=Sum("day8")).filter(sum__gt=thres).distinct().count()
    t1=alltopics.filter(TOPIC=topic["TOPIC"]).values("TARGET").annotate(sum=Sum("day8")).filter(sum__gt=thres).distinct().count()
    list1["clusters"]=int((t1+t)/2)
    arr[i]=list1
    i=i+1
    list1={}
    list1["day"]=2
    list1["topic"]=topic["TOPIC"].encode('latin-1')
    list1["total"]=topic["d2"]
    t=alltopics.filter(TOPIC=topic["TOPIC"]).values("SOURCE").annotate(sum=Sum("day7")).filter(sum__gt=thres).distinct().count()
    t1=alltopics.filter(TOPIC=topic["TOPIC"]).values("TARGET").annotate(sum=Sum("day7")).filter(sum__gt=thres).distinct().count()
    list1["clusters"]=int((t1+t)/2)
    arr[i]=list1
    i=i+1
    list1={}
    list1["day"]=3
    list1["topic"]=topic["TOPIC"].encode('latin-1')
    list1["total"]=topic["d3"]
    t=alltopics.filter(TOPIC=topic["TOPIC"]).values("SOURCE").annotate(sum=Sum("day6")).filter(sum__gt=thres).distinct().count()
    t1=alltopics.filter(TOPIC=topic["TOPIC"]).values("TARGET").annotate(sum=Sum("day6")).filter(sum__gt=thres).distinct().count()
    list1["clusters"]=int((t1+t)/2)
    arr[i]=list1
    i=i+1
    list1={}
    list1["day"]=4
    list1["topic"]=topic["TOPIC"].encode('latin-1')
    list1["total"]=topic["d4"]
    t=alltopics.filter(TOPIC=topic["TOPIC"]).values("SOURCE").annotate(sum=Sum("day5")).filter(sum__gt=thres).distinct().count()
    t1=alltopics.filter(TOPIC=topic["TOPIC"]).values("TARGET").annotate(sum=Sum("day5")).filter(sum__gt=thres).distinct().count()
    list1["clusters"]=int((t1+t)/2)
    arr[i]=list1
    i=i+1
    list1={}
    list1["day"]=5
    list1["topic"]=topic["TOPIC"].encode('latin-1')
    list1["total"]=topic["d5"]
    t=alltopics.filter(TOPIC=topic["TOPIC"]).values("SOURCE").annotate(sum=Sum("day4")).filter(sum__gt=thres).distinct().count()
    t1=alltopics.filter(TOPIC=topic["TOPIC"]).values("TARGET").annotate(sum=Sum("day4")).filter(sum__gt=thres).distinct().count()
    list1["clusters"]=int((t1+t)/2)

    arr[i]=list1
    i=i+1
    list1={}
    list1["day"]=6
    list1["topic"]=topic["TOPIC"].encode('latin-1')
    list1["total"]=topic["d6"]
    t=alltopics.filter(TOPIC=topic["TOPIC"]).values("SOURCE").annotate(sum=Sum("day3")).filter(sum__gt=thres).distinct().count()
    t1=alltopics.filter(TOPIC=topic["TOPIC"]).values("TARGET").annotate(sum=Sum("day3")).filter(sum__gt=thres).distinct().count()
    list1["clusters"]=int((t1+t)/2)
    arr[i]=list1
    i=i+1
    list1={}
    list1["day"]=7
    list1["topic"]=topic["TOPIC"].encode('latin-1')
    list1["total"]=topic["d7"]
    t=alltopics.filter(TOPIC=topic["TOPIC"]).values("SOURCE").annotate(sum=Sum("day1")).filter(sum__gt=thres).distinct().count()
    t1=alltopics.filter(TOPIC=topic["TOPIC"]).values("TARGET").annotate(sum=Sum("day1")).filter(sum__gt=thres).distinct().count()
    list1["clusters"]=int((t1+t)/2)

    arr[i]=list1
    i=i+1
    
print arr