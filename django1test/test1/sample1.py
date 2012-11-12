'''
Created on Nov 2, 2012

@author: saruchi
'''
from test1.models import aggregate2,intra_day
from django.core.files import File

for i in aggregate2.objects.filter(time_interval='week4'):
    p1 = aggregate2(time_interval='month1',month=i.month, topic=i.topic,no_users=i.no_users)
    p1.save()
    print i.month()
    i.delete()

for i in aggregate2.objects.filter(time_interval='week3'):
    p1 = aggregate2(time_interval='week4',month=i.month, topic=i.topic,no_users=i.no_users)
    p1.save()
    print i.month()
    i.delete()

for i in aggregate2.objects.filter(time_interval='week2'):
    p1 = aggregate2(time_interval='week3',month=i.month, topic=i.topic,no_users=i.no_users)
    p1.save()
    print i.month()
    i.delete()

for i in aggregate2.objects.filter(time_interval='week1'):
    p1 = aggregate2(time_interval='week2',month=i.month, topic=i.topic,no_users=i.no_users)
    p1.save()
    print i.month()
    i.delete()

for i in aggregate2.objects.filter(time_interval__in =['day1','day2','day3','day4','day5','day6','day7','day8''day9','day10','day11']):
    
    p1 = aggregate2(time_interval='week1',month=i.month, topic=i.topic,no_users=i.no_users)
    p1.save()
    print i.month()
    i.delete()


month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
time=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10','day11','week1','week2','week3','week4','month1','month2','month3']
time_list=['a','a','a','a','a','a','a','a','a','a','a']
usr_list=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
topic_list=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
time_usr=[0,0,0,0,0,0,0,0]
max_month=0
max_month1=0
counter=0

with open('log-comm.11.out', 'r') as f:
    myfile = File(f)
    
    for line in myfile:
        a=line.split(' ')
        counter=counter+1
# for calculating correct interval label for insertion
        tinsert='a';
        for i in range(0,11):
            if time_list[i]=='a':
                time_list[i]=a[3]
                tinsert=time[i]
                break
            else:
                if time_list[i]==a[3]:
                    tinsert=time[i]
                    break
                   
        
        #print tinsert       
        #print a[3]
        
#estimate correct topic for insertion        
        if len(a)==9:
            b= a[8] 
        elif len(a)==10:
            b= a[8]+a[9]
        elif len(a)==11:
            b= a[8]+a[9]+a[10]
        elif len(a)==11:
            b= a[8]+a[9]+a[10]+a[11]
            
#estimate correct users for each topic and each given day    
        x=time.index(tinsert)
        if b in topic_list[x]:
            y=topic_list[x].index(b)
            usr_list[x][y]=int(usr_list[x][y])+1
        else:
            topic_list[x].append(b)
            y=topic_list[x].index(b)
            usr_list[x].append(1)
        y=topic_list[x].index(b)
        
        max_month=month.index(a[2]);
        if counter==0:
            max_month1=month.index(a[2]);
         
        #inserts values in aggregate2 
        #p1 = aggregate2(time_interval=tinsert,month=a[2], topic=b,no_users=int(usr_list[x][y]))
        #p1.save()
        
        #calculate no of users in each time interval
        t=a[4]
        interval=t.split(':')
        if int(interval[0])>= 3 and int(interval[0])<6:
            time_usr[0]=time_usr[0]+1
        elif int(interval[0])>= 6 and int(interval[0])<9:
            time_usr[1]=time_usr[1]+1
        elif int(interval[0])>= 9 and int(interval[0])<12:
            time_usr[2]=time_usr[2]+1
        elif int(interval[0])>= 12 and int(interval[0])<15:
            time_usr[3]=time_usr[3]+1
        elif int(interval[0])>= 15 and int(interval[0])<18:
            time_usr[4]=time_usr[4]+1
        elif int(interval[0])>= 18 and int(interval[0])<21:
            time_usr[5]=time_usr[5]+1
        elif int(interval[0])>= 21 and int(interval[0])<24:
            time_usr[6]=time_usr[6]+1
        elif int(interval[0])>= 0 and int(interval[0])<3:
            time_usr[7]=time_usr[7]+1
        
        #insert values in intra_day
    #p2 = intra_day(time3_6=time_usr[0],time6_9=time_usr[1],time9_12=time_usr[2],time12_15=time_usr[3],time15_18=time_usr[4],
     #        time18_21=time_usr[5],time21_24=time_usr[6],time0_3=time_usr[7])
    #p2.save()
        
        
        
    #for i in range(0,8):
        #print time_usr[i]
        
        
myfile.closed
f.closed

#for intra_day take already existing values and simply add the above obtained values in each interval
for i in intra_day.objects.all():
    time_usr[0]=i.time3_6 + time_usr[0]
    time_usr[1]=i.time6_9 + time_usr[1]
    time_usr[2]=i.time9_12 + time_usr[2]
    time_usr[3]=i.time12_15 + time_usr[3]
    time_usr[4]=i.time15_18 + time_usr[4]
    time_usr[5]=i.time18_21 + time_usr[5]
    time_usr[6]=i.time21_24 + time_usr[6]
    time_usr[7]=i.time0_3 + time_usr[7]
    break
    #print time_usr[0]
    #print i.time3_6
    #print time_usr[1]
    #print i.time6_9
    #print time_usr[2]
    #print i.time9_12
    #print time_usr[3]
    #print i.time12_15

p2 = intra_day(time3_6=time_usr[0],time6_9=time_usr[1],time9_12=time_usr[2],time12_15=time_usr[3],time15_18=time_usr[4],
             time18_21=time_usr[5],time21_24=time_usr[6],time0_3=time_usr[7])
p2.save()
        

#for aggregate2- store month. storing year is not required because i dont save the data beyond 4 months
#replace tag of day1-9 by week1
#replace week1-week2 wek 3-4 
#check moth of week 4
#week4+month1 in same mnth becomes month 1
#month1-1 becomes mnth 2
#start from bottom i.e. replace months first , den weeks, n den add days data


if max_month!=max_month1:
    max_month=max_month-1

aggregate2.objects.filter(month=(max_month-4)%12+1).delete()   
for i in aggregate2.objects.filter(month=(max_month-3)%12+1,time_interval='month2'):
    p1 = aggregate2(time_interval='month3',month=i.month, topic=i.topic,no_users=i.no_users)
    p1.save()
    print i.month()
    i.delete()
         
for i in aggregate2.objects.filter(month=(max_month-2)%12+1,time_interval='month1'):
    p1 = aggregate2(time_interval='month2',month=i.month, topic=i.topic,no_users=i.no_users)
    p1.save()
    print i.month()
    i.delete()