from test1.models import clustertopicinter,locationlist,Nodes,r1_nodes
from django.db.models import Count,Sum
#tests=locationtopicdata.objects.values("TOPIC").annotate(cnt=Count("TOPIC")) 
#for test in tests:
#    print test["cnt"]
#locations=locationtopicinter.objects.all()
#tests=Nodes.objects.values("LABEL").annotate(id=Count("ID")).order_by("LABEL")

clusters=clustertopicinter.objects.all()
for r in r1_nodes.objects.all():
    ts=clusters.filter(clusterID=r.ID)
    for t in ts:
        t.size=r.SIZE
        t.save()