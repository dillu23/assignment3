from test1.models import locationlist
from django.core.files import File

with open('log-graph.out', 'r') as f:
    myfile = File(f)
    for line in myfile:
        a=line.split(" ")
        if a[1]=="node":
            loc=a[3]
            try:
                b=locationlist.objects.get(LOCATION=loc)
            except locationlist.DoesNotExist:
                b=locationlist(LOCATION=loc)
                b.save()
            
        else:
            exit()