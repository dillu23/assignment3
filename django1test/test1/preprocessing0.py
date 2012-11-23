from test1.models import r1_edges,Nodes,locationlist


for edge in r1_edges.objects.all():
    if edge.WEIGHT<20:
        edge.delete()

for node in Nodes.objects.all():
    try:
        locationrow1=locationlist.objects.get(LOCATION=node.LABEL)
    except locationlist.DoesNotExist:
        locationrow=locationlist(LOCATION=node.LABEL)
        locationrow.save()
