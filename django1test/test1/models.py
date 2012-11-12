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
#
# friend graph edge class
class Edges(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    WEIGHT=models.IntegerField();
    #node2=models.ForeignKey(Nodes);
    
class r_nodes(models.Model):
    ID=models.IntegerField();
    ID.primary_key=True;
    LABEL=models.CharField(max_length=30);
    SIZE=models.IntegerField();
    
class r_edges(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    WEIGHT=models.IntegerField();

