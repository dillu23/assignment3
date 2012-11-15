from django.core.files import File
from test1.models import Nodes,edgedata,datacount,topicdata,timedata


time="3"
location="asgard"
try:
    p=timedata.objects.get(TIME=time,LOCATION=location)
except topicdata.DoesNotExist:
    p=topicdata(TIME=time,LOCATION=location,day1=1,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
    p.save()
else:
    p.day1=p.day1+1
    p.save()
