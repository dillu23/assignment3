from test1.models import Nodes,Edges,r1_edges,edgedata
#from django.core.files import File

#with open('clustering.txt', 'r') as f:
#    myfile = File(f)
    
#    for line in myfile:

count=0
for edge in Edges.objects.all():
    r=edge.SOURCE
    srcnode=Nodes.objects.get(ID=r)
    r=edge.TARGET
    tarnode=Nodes.objects.get(ID=r)
    if srcnode.LABEL2==tarnode.LABEL2:
        edge2=edgedata(SOURCE=srcnode.ID,TARGET=tarnode.ID,LABEL=srcnode.LABEL2,CLUSTERSOURCE=srcnode.ID,CLUSTERTARGET=tarnode.ID,WEIGHT=1,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
        edge2.save()
        count=count+1
    else:
        try:
            p=r1_edges.objects.get(SOURCE=srcnode.LABEL2,TARGET=tarnode.LABEL2)
        except r1_edges.DoesNotExist:
            try:
                p=r1_edges.objects.get(SOURCE=srcnode.LABEL2,TARGET=tarnode.LABEL2)
            except r1_edges.DoesNotExist:
                print ""
            else:
                edge2=edgedata(SOURCE=srcnode.ID,TARGET=tarnode.ID,LABEL=-23,CLUSTERSOURCE=srcnode.LABEL2,CLUSTERTARGET=tarnode.LABEL2,WEIGHT=1,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
                edge2.save()
                count=count+1
        else:
            edge2=edgedata(SOURCE=srcnode.ID,TARGET=tarnode.ID,LABEL=-23,CLUSTERSOURCE=srcnode.LABEL2,CLUSTERTARGET=tarnode.LABEL2,WEIGHT=1,day1=0,day2=0,day3=0,day4=0,day5=0,day6=0,day7=0,day8=0,day9=0,day10=0,day11=0,day12=0,day13=0,day14=0,day15=0,week1=0,week2=0,week3=0,week4=0,month1=0,month2=0,month3=0)
            edge2.save()
            count=count+1
        
        