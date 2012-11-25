from test1.models import edgedata
from django.db.models import Count
import json

#tests=edgedata.objects.exclude(week1=0).order_by("-week1")[0:25]
tests=edgedata.objects.values("TOPIC","day8","day2","day3","day4","day5","day6","day7","week1","week2","week3","week4","month1","month2","month3","month4").annotate(cnt=Count("TOPIC")).order_by("-week1")[0:50]
arr=[""]*tests.count()
i=0;
for test in tests:
    list1={}
    list1["topic"]=test["TOPIC"]
    list1["day1"]=test["day8"]
    list1["day2"]=test["day7"]
    list1["day3"]=test["day6"]
    list1["day4"]=test["day5"]
    list1["day5"]=test["day4"]
    list1["day6"]=test["day3"]
    list1["day7"]=test["day2"]
    list1["week1"]=test["week4"]
    list1["week2"]=test["week1"]
    list1["week3"]=test["week4"]
    list1["month1"]=12
    list1["month2"]=11
    list1["month3"]=11
    arr[i]=list1
    i=i+1
    
print json.dumps(arr)