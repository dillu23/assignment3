from test1.models import Nodes,Edges,r_nodes,r_edges
import copy

def findclique(list, size, target):
    if i==1:
        list[target]=1
        return True
    else:
        list1=copy.copy(list)
        list1[target]=1
        t=False
        nbrs=getneighbors(target)
        for nbr in nbrs:
            r=findclique(list,size,target)
            if r==True:
                print "HI"
                
def findcluster(list,size,target):
    list2=copy.copy(list)
    list2[target]=1;
    nbrs=getneighbors(target)
                    
# returns list
def getneighbors(target):
    size=0;
    count=Edges.objects.filter(SOURCE=target).count()+Edges.objects.filter(TARGET=target).count()
    list1=[0]*count
    edges=Edges.objects.filter(SOURCE=target)
    for edge in edges:
        list1[size]= edge.TARGET
        size=size+1
    edges=Edges.objects.filter(TARGET=target)
    
    for edge in edges:
        list1[size]= edge.SOURCE
        size=size+1
    return list1



# returns boolean


def isneighbor(source, target):
    try:
        edge=Edges.objects.get(SOURCE=source,TARGET=target)
    except Edges.DoesNotExist:
        try: 
            edge=Edges.objects.get(SOURCE=target,TARGET=source)
        except Edges.DoesNotExist:
            return False
        else: return True
    else:
        return True
    
def addclique(list1):
    print "HI"
    
num=7
node_count= Nodes.objects.all().count()
marker=[0]*node_count
nodes=Nodes.objects.all()

for i in xrange(num,2,-1):
    for node in nodes:
        l=findclique(marker,i,node.ID)
        if l:
            addclique(marker)
        marker=[0]*node_count
#Edges.objects.filter(TARGET=target).count()

print isneighbor(1,2)