def preprocess3(filename):
    from django.db.models.sql.datastructures import Date
    from test1.models import Nodes,r1_edges,edgedata,locationtopicdata,locationtimedata,topiclist
    from django.core.files import File
    from test1.clean import cleandata
    import json
    
    monthdict={"Jan":0,"Feb":1,"Mar":2,"Apr":3,"May":4,"Jun":5,"Jul":6,"Aug":7,"Sep":8,"Oct":9,"Nov":10,"Dec":11}
    monthinv={0:"Jan",1:"Feb",2:"Mar",3:"Apr",4:"May",5:"Jun",6:"Jul",7:"Aug",8:"Sep",9:"Oct",10:"Nov",11:"Dec"}
    r=0
    tmonth=1;
    with open('data/data.json','r') as f:
        myfile=File(f)
        for line in myfile:
            list1=json.loads(line)
            r=list1["day"]
            tmonth=monthdict[list1["month"]]
    
    
    k=-1
    nodes=Nodes.objects.all()
    r_edges=r1_edges.objects.all()
    with open(filename, 'r') as f:
        myfile = File(f)
        counter=0
        for line in myfile:
            a=line.split(' ')
            counter=counter+1
            topic1=a[8]
            if len(a)==10:
                topic1=topic1+" "+a[9]
            topic1=topic1[:-1]
            try:
                topiclist.objects.get(TOPIC=topic1)
            except topiclist.DoesNotExist:
                topicrow2=topiclist(TOPIC=topic1)
                topicrow2.save()
            
            if r!=int(a[3]):
                k=k+1
                print k
                if int(r/8)!=int(int(a[3])/8):
                    r=int(a[3])
                    cleandata("week",int(r/8))
                r=int(a[3])
            
            if int(tmonth%4)!=int(monthdict[a[2]]%4):
                cleandata("month",int(tmonth%4))
                tmonth=int(monthdict[a[2]])
            
            b=a[7].split('-')
            tar=int(b[1][:-1])
            src=int(b[0])
            location="inter"
            if nodes.get(ID=tar).LABEL==nodes.get(ID=src).LABEL:
                location=nodes.get(ID=tar).LABEL
            time=int(int(a[4].split(":")[0])/3)
            tar=nodes.get(ID=tar).LABEL2
            src=nodes.get(ID=src).LABEL2
            if src>tar:
                t=tar
                tar=src
                src=t
            try:
                r_edges.get(SOURCE=src,TARGET=tar)
            except r1_edges.DoesNotExist:
                dump=0;
            else:
                try:
                    p=edgedata.objects.get(SOURCE=src,TARGET=tar,TOPIC=topic1)
                except edgedata.DoesNotExist:
                    p=edgedata(SOURCE=src,TARGET=tar,TOPIC=topic1,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0,month4=0)
                if k==0:
                    p.day1=p.day1+1;
                if k==1:
                    p.day2=p.day2+1;
                if k==2:
                    p.day3=p.day3+1;
                if k==3:
                    p.day4=p.day4+1;
                if k==4:
                    p.day5=p.day5+1;
                if k==5:
                    p.day6=p.day6+1;
                if k==6:
                    p.day7=p.day7+1;
                if k==7:
                    p.day8=p.day8+1;
                if k==8:
                    p.day9=p.day9+1;
                if k==9:
                    p.day10=p.day10+1;
                if k==10:
                    p.day11=p.day11+1;
                if k==11:
                    p.day12=p.day12+1;
                if k==12:
                    p.day13=p.day13+1;
                if k==13:
                    p.day14=p.day14+1;
                if k==14:
                    p.day15=p.day15+1;
                if int(r/8)==0:
                    p.week1=p.week1+1;
                if int(r/8)==1:
                    p.week2=p.week2+1;
                if int(r/8)==2:
                    p.week3=p.week3+1;
                if int(r/8)==3:
                    p.week4=p.week4+1;
                if int(tmonth%4)==0:
                    p.month1=p.month1+1;
                if int(tmonth%4)==1:
                    p.month2=p.month2+1;
                if int(tmonth%4)==2:
                    p.month3=p.month3+1;
                if int(tmonth%4)==3:
                    p.month4=p.month4+1;
                
                p.save();
            try:
                lcttopic=locationtopicdata.objects.get(TOPIC=topic1,LOCATION=location)
            except locationtopicdata.DoesNotExist:
                lcttopic=locationtopicdata(TOPIC=topic1,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0,month4=0)
            try:
                lcttime=locationtimedata.objects.get(TIME=time,LOCATION=location)
            except locationtimedata.DoesNotExist:
                lcttime=locationtimedata(TIME=time,LOCATION=location,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0,month4=0)
            if k==0:
                lcttopic.day1=lcttopic.day1+1;
                lcttime.day1=lcttime.day1+1;
            if k==1:
                lcttopic.day2=lcttopic.day2+1;
                lcttime.day2=lcttime.day2+1;
            if k==2:
                lcttopic.day3=lcttopic.day3+1;
                lcttime.day3=lcttime.day3+1;
            if k==3:
                lcttopic.day4=lcttopic.day4+1;
                lcttime.day4=lcttime.day4+1;
            if k==4:
                lcttopic.day5=lcttopic.day5+1;
                lcttime.day5=lcttime.day5+1;
            if k==5:
                lcttopic.day6=lcttopic.day6+1;
                lcttime.day6=lcttime.day6+1;
            if k==6:
                lcttopic.day7=lcttopic.day7+1;
                lcttime.day7=lcttime.day7+1;
            if k==7:
                lcttopic.day8=lcttopic.day8+1;
                lcttime.day8=lcttime.day8+1;
            if k==8:
                lcttopic.day9=lcttopic.day9+1;
                lcttime.day9=lcttime.day9+1;
            if k==9:
                lcttopic.day10=lcttopic.day10+1;
                lcttime.day10=lcttime.day10+1;
            if k==10:
                lcttopic.day11=lcttopic.day11+1;
                lcttime.day11=lcttime.day11+1;
            if k==11:
                lcttopic.day12=lcttopic.day12+1;
                lcttime.day12=lcttime.day12+1;
            if k==12:
                lcttopic.day13=lcttopic.day13+1;
                lcttime.day13=lcttime.day1+13;
            if k==13:
                lcttopic.day14=lcttopic.day14+1;
                lcttime.day14=lcttime.day14+1;
            if k==14:
                lcttopic.day15=lcttopic.day15+1;
                lcttime.day15=lcttime.day15+1;
            if int(r/8)==0:
                lcttopic.week1=lcttopic.week1+1;
                lcttime.week1=lcttime.week1+1;
            if int(r/8)==1:
                lcttopic.week2=lcttopic.week2+1;
                lcttime.week2=lcttime.week2+1;
            if int(r/8)==2:
                lcttopic.week3=lcttopic.week3+1;
                lcttime.week3=lcttime.week3+1;
            if int(r/8)==3:
                lcttopic.week4=lcttopic.week4+1;
                lcttime.week4=lcttime.week4+1;
            if int(tmonth%4)==0:
                lcttopic.month1=lcttopic.month1+1;
                lcttime.month1=lcttime.month1+1;
            if int(tmonth%4)==1:
                lcttopic.month2=lcttopic.month2+1;
                lcttime.month2=lcttime.month2+1;
            if int(tmonth%4)==2:
                lcttopic.month3=lcttopic.month3+1;
                lcttime.month3=lcttime.month3+1;
            if int(tmonth%4)==3:
                lcttopic.month4=lcttopic.month4+1;
                lcttime.month4=lcttime.month4+1;
            lcttopic.save()
            lcttime.save()
    
    
    handle=open("data/data.json","r+")
    arr={}
    arr["day"]=r
    arr["month"]=monthinv[t]