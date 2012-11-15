from test1.models import r1_nodes
import json


nodes=r1_nodes.objects.all()
count=r1_nodes.objects.all().count()
#handle=open("dump.txt","r+")
i=0
arr =[""]*count
for node in nodes:
    #handle.write(node.LABEL+"\n")
    list1={}
    list1["ID"]=node.ID
    list1["LABEL"]=node.LABEL
    arr[i]=list1
    i=i+1
    
print json.dumps(arr) 