from django.db import models

#aggregate table


class aggregate2(models.Model):
    time_interval=models.CharField(max_length=30)
    month=models.CharField(max_length=30)
    topic = models.CharField(max_length=30)
    no_users = models.IntegerField()
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#cluster table
#stores top 5 locations and discussion topics for each cluster
class cluster(models.Model):
    time_interval=models.CharField(max_length=30)
    month=models.CharField(max_length=30)
    cluster_id = models.CharField(max_length=30)
    location1=models.CharField(max_length=30)
    location2=models.CharField(max_length=30)
    location3=models.CharField(max_length=30)
    location4=models.CharField(max_length=30)
    location5=models.CharField(max_length=30)
    topic1=models.CharField(max_length=30)
    topic2=models.CharField(max_length=30)
    topic3=models.CharField(max_length=30)
    topic4=models.CharField(max_length=30)
    topic5=models.CharField(max_length=30)
   
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#within day communication table 

class intra_day(models.Model):
    time3_6=models.IntegerField();
    time6_9=models.IntegerField();
    time9_12=models.IntegerField();
    time12_15=models.IntegerField();
    time15_18=models.IntegerField();
    time18_21=models.IntegerField();
    time21_24=models.IntegerField();
    time0_3=models.IntegerField();
    
#-------------------------------------------------------------------------------------------------------------------
#relation of each node and cluster

class node_cluster(models.Model):
    node_id=models.IntegerField();
    cluster_id=models.CharField(max_length=30);
    
    
#
# friend graph nodes class
class Nodes(models.Model):
    
    ID=models.IntegerField();
    ID.primary_key=True;
    LABEL=models.CharField(max_length=30);
    SIZE=models.IntegerField();
    LABEL1=models.IntegerField();
    LABEL2=models.IntegerField();
    LABEL3=models.IntegerField();
    LABEL4=models.IntegerField();
    LABEL5=models.IntegerField();
#
# friend graph edge class
class Edges(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    WEIGHT=models.IntegerField();
    LABEL=models.IntegerField();
    TYPE=models.CharField(max_length=30);
    #node2=models.ForeignKey(Nodes);
    
class r_nodes(models.Model):
    ID=models.IntegerField();
    ID.primary_key=True;
    LABEL=models.IntegerField();
    SIZE=models.IntegerField();
    
class r_edges(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    WEIGHT=models.IntegerField();

class r1_nodes(models.Model):
    ID=models.IntegerField();
    ID.primary_key=True;
    LABEL=models.IntegerField();
    SIZE=models.IntegerField();
    
class r1_edges(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    WEIGHT=models.IntegerField();

class r2_nodes(models.Model):
    ID=models.IntegerField();
    ID.primary_key=True;
    LABEL=models.IntegerField();
    SIZE=models.IntegerField();
    
class r2_edges(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    WEIGHT=models.IntegerField();

class edgedata(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    LABEL=models.IntegerField();
    CLUSTERSOURCE=models.IntegerField();
    CLUSTERTARGET=models.IntegerField();
    WEIGHT=models.IntegerField();
    day1=models.IntegerField();
    day2=models.IntegerField();
    day3=models.IntegerField();
    day4=models.IntegerField();
    day5=models.IntegerField();
    day6=models.IntegerField();
    day7=models.IntegerField();
    day8=models.IntegerField();
    day9=models.IntegerField();
    day10=models.IntegerField();
    day11=models.IntegerField();
    day12=models.IntegerField();
    day13=models.IntegerField();
    day14=models.IntegerField();
    day15=models.IntegerField();
    week1=models.IntegerField();
    week2=models.IntegerField();
    week3=models.IntegerField();
    week4=models.IntegerField();
    month1=models.IntegerField();
    month2=models.IntegerField();
    month3=models.IntegerField();
    
class topicdata(models.Model):
    TOPIC=models.CharField(max_length=30);
    LOCATION=models.CharField(max_length=30);
    day1=models.IntegerField();
    day2=models.IntegerField();
    day3=models.IntegerField();
    day4=models.IntegerField();
    day5=models.IntegerField();
    day6=models.IntegerField();
    day7=models.IntegerField();
    day8=models.IntegerField();
    day9=models.IntegerField();
    day10=models.IntegerField();
    day11=models.IntegerField();
    day12=models.IntegerField();
    day13=models.IntegerField();
    day14=models.IntegerField();
    day15=models.IntegerField();
    week1=models.IntegerField();
    week2=models.IntegerField();
    week3=models.IntegerField();
    week4=models.IntegerField();
    month1=models.IntegerField();
    month2=models.IntegerField();
    month3=models.IntegerField();
    
class timedata(models.Model):
    TIME=models.CharField(max_length=30);
    LOCATION=models.CharField(max_length=30);
    day1=models.IntegerField();
    day2=models.IntegerField();
    day3=models.IntegerField();
    day4=models.IntegerField();
    day5=models.IntegerField();
    day6=models.IntegerField();
    day7=models.IntegerField();
    day8=models.IntegerField();
    day9=models.IntegerField();
    day10=models.IntegerField();
    day11=models.IntegerField();
    day12=models.IntegerField();
    day13=models.IntegerField();
    day14=models.IntegerField();
    day15=models.IntegerField();
    week1=models.IntegerField();
    week2=models.IntegerField();
    week3=models.IntegerField();
    week4=models.IntegerField();
    month1=models.IntegerField();
    month2=models.IntegerField();
    month3=models.IntegerField();
    
class locationlist(models.Model):
    LOCATION=models.CharField(max_length=30);
    
class datacount(models.Model):
    DATECOUNT=models.IntegerField();
    
class topiclist(models.Model):
    TOPIC=models.CharField(max_length=30);