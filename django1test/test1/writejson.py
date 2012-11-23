#from test1.models import topicdata,topiclist
#from django.db.models import Sum
#import json

#topics=topicdata.objects.values("TOPIC").annotate(day8=Sum("day8")).annotate(day7=Sum("day7")).annotate(day6=Sum("day6")).annotate(day5=Sum("day5")).annotate(day4=Sum("day4")).annotate(day3=Sum("day3")).annotate(day2=Sum("day2")).annotate(day1=Sum("day1"))
#topicslist=topiclist.objects.all();
#handle=open("dump.txt","r+")
#count=topicslist.count()
#i=0
#arr =[""]*8
#for i in xrange(1,9):
#    r="day"+str(i)
#   list1={}
#    list1["day"]=r
#    for topic in topicslist:
#        list1[topic.TOPIC]=0
#    arr[i-1]=list1
    
#print arr
#for topic in topics:
#    for i in xrange(1,9):
#        r="day"+str(i)
#        list1=arr[i-1]
#        list1[topic["TOPIC"]]=topic[r]
#        print topic[r]
#print json.dumps(arr)
#handle.write(json.dumps(arr))