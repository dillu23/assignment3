from test1.models import Nodes,Edges,r1_nodes,r1_edges
from django.core.files import File

r1_nodes.objects.all().delete()
r1_edges.objects.all().delete()


# TODO label 
with open('data/clustering.txt','r') as f:
    myfile=File(f)
    for line in myfile:
        a=line.split('\t')
        id1=a[0]
        label1=a[1]
        label2=a[2]
        label3=a[3]
        label4=a[4]
        label5=a[5]
        label6=a[6]
        node=Nodes.objects.get(ID=id1)
        node.LABEL1=label1
        node.LABEL2=label2
        node.LABEL3=label3
        node.LABEL4=label4
        node.LABEL5=label5
        node.LABEL6=label6
        node.save()
        try:
            p = r1_nodes.objects.get(ID=label2)
        except r1_nodes.DoesNotExist:
            node2=r1_nodes(ID=label2,LABEL1=label1,LABEL2=label2,LABEL3=label3,LABEL4=label4,LABEL5=label5,LABEL6=label6,SIZE=1)
            node2.save()
        else:
            p.SIZE=p.SIZE+1
            p.save()

        
    edges=Edges.objects.all();
    nodes=Nodes.objects.all();
    for edge in edges:
        src=nodes.get(ID=edge.SOURCE)
        src=src.LABEL2
        tar=nodes.get(ID=edge.TARGET)
        tar=tar.LABEL2
        if src>tar:
            r=tar
            tar=src
            src=tar
        if tar!=src:
            try:
                p = r1_edges.objects.get(SOURCE=src,TARGET=tar)
            except r1_edges.DoesNotExist:
                edge2=r1_edges(SOURCE=src,TARGET=tar,WEIGHT=1)
                edge2.save()
            else:
                p.WEIGHT=p.WEIGHT+1
                p.save()

