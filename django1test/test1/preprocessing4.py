from test1.models import clustertopicinter, locationtopicinter, edgedata,Nodes
from django.core.files import File

with open('data/log-comm.43.out','r') as f:
    myfile=File(f)
    k=-1;r=0;
    nodes=Nodes.objects.all()
    counter=0
    for line in myfile:
        a=line.split(' ')
        if counter%1000==0:
            print counter
        counter=counter+1
        if int(a[3])!=r:
            k=k+1
            r=int(a[3])
        b=a[7].split('-')
        src=nodes.get(ID=int(b[0]))
        tar=nodes.get(ID=int(b[1][:-1]))
        if src.LABEL==tar.LABEL:
            try:
                lct1=locationtopicinter.objects.get(day=k,locationname=src.LABEL)
            except locationtopicinter.DoesNotExist:
                lct1=locationtopicinter(day=k,locationname=src.LABEL,size=0,inter=0,intra=0,total=0)
            lct1.inter=lct1.inter+2
            lct1.save()
        else:
            try:
                lct1=locationtopicinter.objects.get(day=k,locationname=src.LABEL)
            except locationtopicinter.DoesNotExist:
                lct1=locationtopicinter(day=k,locationname=src.LABEL,size=0,inter=0,intra=0,total=0)
            try:
                lct2=locationtopicinter.objects.get(day=k,locationname=tar.LABEL)
            except locationtopicinter.DoesNotExist:
                lct2=locationtopicinter(day=k,locationname=tar.LABEL,size=0,inter=0,intra=0,total=0)
            lct1.intra=lct1.intra+1
            lct2.intra=lct2.intra+1
            lct1.save()
            lct2.save()
        
        if src.LABEL2==tar.LABEL2:
            try:
                lct1=clustertopicinter.objects.get(day=k,clusterID=src.LABEL2)
            except clustertopicinter.DoesNotExist:
                lct1=clustertopicinter(day=k,clusterID=src.LABEL2,size=0,inter=0,intra=0,total=0)
            lct1.inter=lct1.inter+2
            lct1.save()
        else:
            try:
                lct1=clustertopicinter.objects.get(day=k,clusterID=src.LABEL2)
            except clustertopicinter.DoesNotExist:
                lct1=clustertopicinter(day=k,clusterID=src.LABEL2,size=0,inter=0,intra=0,total=0)
            try:
                lct2=clustertopicinter.objects.get(day=k,clusterID=tar.LABEL2)
            except clustertopicinter.DoesNotExist:
                lct2=clustertopicinter(day=k,clusterID=tar.LABEL2,size=0,inter=0,intra=0,total=0)
            lct1.intra=lct1.intra+1
            lct2.intra=lct2.intra+1
            lct1.save()
            lct2.save()