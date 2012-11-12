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
            node=Nodes(ID=id1,LABEL=a[3],SIZE=1)
            node.save()
        elif a[1]=="edge":
            b=a[2].split('-')
            edge=Edges(SOURCE=b[0],TARGET=b[1],WEIGHT=1)
            counter=counter+1
            edge.save()