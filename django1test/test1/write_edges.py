from test1.models import Edges

edges=Edges.objects.all()
handle=open("edges.txt","r+")
for edge in edges: 
 #   print str(edge.SOURCE) + " "+str(edge.TARGET)
    handle.write(str(edge.SOURCE) + " "+str(edge.TARGET)+"\n")