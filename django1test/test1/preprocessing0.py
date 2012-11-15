from test1.models import r1_edges

for edge in r1_edges.objects.all():
    if edge.WEIGHT<20:
        edge.delete()