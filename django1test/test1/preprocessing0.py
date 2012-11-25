from test1.models import r1_edges,Nodes,locationlist,Edges, locationtopicdata


#for edge in r1_edges.objects.all():
#    if edge.WEIGHT<20:
        #edge.delete()

#for node in Nodes.objects.all():
    #try:
        #locationrow1=locationlist.objects.get(LOCATION=node.LABEL)
    #except locationlist.DoesNotExist:
        #locationrow=locationlist(LOCATION=node.LABEL)
        #locationrow.save()

#nodes=Nodes.objects.all()

#for edge in Edges.objects.all():
#    src=nodes.get(ID=edge.SOURCE).LABEL2
#    if src==nodes.get(ID=edge.TARGET).LABEL2:
        
 #       edge.LABEL1=src
#        print "hi"
  #      edge.save()
  
for r in locationtopicdata.objects.all():
    loc=r.LOCATION
    if loc[-1]=="\n":
        print "aye"
        r.LOCATION=r.LOCATION[:-1]
        r.save()
        