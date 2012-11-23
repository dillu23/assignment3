from test1.models import r1_nodes,r1_edges
from django.db.models import Sum
import json

handle=open("data/names.json","r+")

nodes=r1_nodes.objects.all()
count=nodes.count()
arr=[""]*count

i=0
for node in nodes:
        list1={}
        list1["name"]="0."+str(node.LABEL1)+"."+str(node.LABEL2)+"."+str(node.LABEL3)#+"."+str(node.LABEL4)
        list1["size"]=node.SIZE
        arr[i]=list1
        i=i+1
        
handle.write(json.dumps(arr))
handle=open("data/edges.json","r+")        
edges=r1_edges.objects.all()
count=edges.count()
arr=[""]*count
i=0
for edge in edges:
    list1={}
    node=nodes.get(ID=edge.SOURCE)
    list1["source"]="0."+str(node.LABEL1)+"."+str(node.LABEL2)+"."+str(node.LABEL3)#+"."+str(node.LABEL4)
    node=nodes.get(ID=edge.TARGET)
    list1["target"]="0."+str(node.LABEL1)+"."+str(node.LABEL2)+"."+str(node.LABEL3)#+"."+str(node.LABEL4)
    list1["weight"]=edge.WEIGHT
    arr[i]=list1
    i=i+1
    
handle.write(json.dumps(arr))