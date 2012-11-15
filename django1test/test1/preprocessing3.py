from test1.models import Nodes,edgedata,datacount,topicdata,timedata
from django.core.files import File

# move data
k=0;
r=datacount.objects.all()
for i in r:
    k=r.DATECOUNT

for i in edgedata.objects.all():
    i.month3=i.month2;i.month2=i.month1;i.month1=i.week1+i.week2+i.week3+i.week4;i.week4=i.week3;
    i.week3=i.week2;i.week2=i.week1;i.week1=i.day1+i.day2+i.day3+i.day4+i.day5+i.day6+i.day7+i.day8+i.day9+i.day10+i.day11+i.day12+i.day13+i.day14+i.day15;
    i.save();
    
for i in topicdata.objects.all():
    i.month3=i.month2;i.month2=i.month1;i.month1=i.week1+i.week2+i.week3+i.week4;i.week4=i.week3;
    i.week3=i.week2;i.week2=i.week1;i.week1=i.day1+i.day2+i.day3+i.day4+i.day5+i.day6+i.day7+i.day8+i.day9+i.day10+i.day11+i.day12+i.day13+i.day14+i.day15;
    i.save();
    
for i in timedata.objects.all():
    i.month3=i.month2;i.month2=i.month1;i.month1=i.week1+i.week2+i.week3+i.week4;i.week4=i.week3;
    i.week3=i.week2;i.week2=i.week1;i.week1=i.day1+i.day2+i.day3+i.day4+i.day5+i.day6+i.day7+i.day8+i.day9+i.day10+i.day11+i.day12+i.day13+i.day14+i.day15;
    i.save();
r=0;
k=-1;
with open('log-comm.00.out', 'r') as f:
    myfile = File(f)
    for line in myfile:
        a=line.split(' ')
        print str(r)+ " and "+ str(a[3])
        if int(r)!=int(a[3]):
            k=k+1
            r=a[3]
        if k==0:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day1=p.day1+1;
                    p.save();
            else:
                p.day1=p.day1+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=1,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day1=p.day1+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=1,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day1=p.day1+1
                p.save()
        
        if k==1:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day2=p.day2+1;
                    p.save();
            else:
                p.day2=p.day2+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=1,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day2=p.day2+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=1,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day2=p.day2+1
                p.save()
        if k==2:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day3=p.day3+1;
                    p.save();
            else:
                p.day3=p.day3+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=1,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day3=p.day3+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=1,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day3=p.day3+1
                p.save()
        if k==3:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day4=p.day4+1;
                    p.save();
            else:
                p.day4=p.day4+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=1,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day4=p.day4+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=1,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day4=p.day4+1
                p.save()
        
        if k==4:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day5=p.day5+1;
                    p.save();
            else:
                p.day5=p.day5+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=1,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day5=p.day5+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=1,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day5=p.day5+1
                p.save()
        
        if k==5:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day6=p.day6+1;
                    p.save();
            else:
                p.day6=p.day6+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=1,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day6=p.day6+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=1,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day6=p.day6+1
                p.save()
        
        if k==6:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day7=p.day7+1;
                    p.save();
            else:
                p.day7=p.day7+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=1,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day7=p.day7+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=1,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day7=p.day7+1
                p.save()		
        
        if k==7:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day8=p.day8+1;
                    p.save();
            else:
                p.day8=p.day8+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=1,day9=0,day40=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day8=p.day8+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=1,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day8=p.day8+1
                p.save()
        if k==8:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day9=p.day9+1;
                    p.save();
            else:
                p.day9=p.day9+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=1,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day9=p.day9+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=1,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day9=p.day9+1
                p.save()
        
        if k==9:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day10=p.day10+1;
                    p.save();
            else:
                p.day10=p.day10+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=1,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day10=p.day10+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=1,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day10=p.day10+1
                p.save()
        
        if k==10:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day11=p.day11+1;
                    p.save();
            else:
                p.day11=p.day11+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day40=0,day11=1,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day11=p.day11+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=1,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day11=p.day11+1
                p.save()
        
        if k==11:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day12=p.day12+1;
                    p.save();
            else:
                p.day12=p.day12+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=1,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day12=p.day12+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=1,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day12=p.day12+1
                p.save()
        
        if k==12:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day13=p.day13+1;
                    p.save();
            else:
                p.day13=p.day13+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day40=0,day11=0,day12=0,day13=1,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day13=p.day13+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=1,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day13=p.day13+1
                p.save
        
        if k==13:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day14=p.day14+1;
                    p.save();
            else:
                p.day14=p.day14+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day14=p.day14+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=1,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day14=p.day14+1
                p.save()
        
        if k==14:
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            try:
                p=edgedata.objects.get(SOURCE=src,TARGET=tar)
            except edgedata.DoesNotExist:
                try:
                    p=edgedata.objects.get(SOURCE=tar,TARGET=src)
                except edgedata.DoesNotExist:
                    print "doesn't exist"
                else:
                    p.day15=p.day15+1;
                    p.save();
            else:
                p.day15=p.day15+1;
                p.save();
            
            topic=a[8];
            location="inter"
            sourcenode=Nodes.objects.get(ID=src)
            targetnode=Nodes.objects.get(ID=tar)
            if sourcenode.LABEL==targetnode.LABEL:
                location=sourcenode.LABEL                                        
            time=int(int(a[4].split(":")[0])/3)
            time=str(time)
            try:
                p=topicdata.objects.get(TOPIC=topic,LOCATION=location)
            except topicdata.DoesNotExist:
                p=topicdata(TOPIC=topic,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=1,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day15=p.day15+1
                p.save()
                
            try:
                p=timedata.objects.get(TIME=time,LOCATION=location)
            except timedata.DoesNotExist:
                p=timedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=1,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                p.save()
            else:
                p.day15=p.day15+1
                p.save()