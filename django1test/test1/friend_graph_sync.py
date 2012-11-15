from test1.models import Nodes,Edges
from django.core.files import File

Nodes.objects.all().delete()
Edges.objects.all().delete()

with open('log-graph.out','r') as f:
    counter=0;
    myfile=File(f)
    for line in myfile:
        a=line.split(' ')
        counter=counter+1;
        if a[1]=="node":
            id1=a[2][:-1]
            node=Nodes(ID=id1,LABEL=a[3],SIZE=1,LABEL1=-1,LABEL2=-2,LABEL3=-3,LABEL4=-4,LABEL5=-5)
            node.save()
        elif a[1]=="edge":
            b=a[2].split('-')
            b[0]=int(b[0])
            b[1]=int(b[1])
            if b[0]<b[1]:
                src=b[0]
                tar=b[1]
            else:
                src=b[1]
                tar=b[0]
            try:
                p=Edges.objects.get(SOURCE=src,TARGET=tar)
            except:
                edge=Edges(SOURCE=src,TARGET=tar,WEIGHT=1,LABEL=0,TYPE="friendsgraph")
                counter=counter+1
                edge.save()