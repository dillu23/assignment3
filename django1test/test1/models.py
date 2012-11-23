from django.db import models

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
    LABEL6=models.IntegerField();

class Edges(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    LABEL1=models.IntegerField();
    
class r1_nodes(models.Model):
    ID=models.IntegerField();
    ID.primary_key=True;
    LABEL1=models.IntegerField();
    LABEL2=models.IntegerField();
    LABEL3=models.IntegerField();
    LABEL4=models.IntegerField();
    LABEL5=models.IntegerField();
    LABEL6=models.IntegerField();
    SIZE=models.IntegerField();
    
class r1_edges(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    WEIGHT=models.IntegerField();
    
class r2_nodes(models.Model):
    ID=models.IntegerField();
    ID.primary_key=True;
    LABEL1=models.IntegerField();
    LABEL2=models.IntegerField();
    LABEL3=models.IntegerField();
    LABEL4=models.IntegerField();
    LABEL5=models.IntegerField();
    LABEL6=models.IntegerField();
    SIZE=models.IntegerField();
    
class r2_edges(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    WEIGHT=models.IntegerField();

class edgedata(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    TOPIC=models.CharField(max_length=30);
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
    month4=models.IntegerField();

class clustertopicdata(models.Model):
    SOURCE=models.IntegerField();
    TARGET=models.IntegerField();
    TOPIC=models.CharField(max_length=30);
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
    
class locationtopicdata(models.Model):
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
    month4=models.IntegerField();

class locationtimedata(models.Model):
    TIME=models.IntegerField();
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
    month4=models.IntegerField();

class toptopic(models.Model):
    DATE=models.DateField();
    LOCATION=models.CharField(max_length=30);
    TOPIC1=models.CharField(max_length=30);
    TOPIC2=models.CharField(max_length=30);
    TOPIC3=models.CharField(max_length=30);
    TOPIC4=models.CharField(max_length=30);
    TOPIC5=models.CharField(max_length=30);
    TOPIC6=models.CharField(max_length=30);
    TOPIC7=models.CharField(max_length=30);
    TOPIC8=models.CharField(max_length=30);
    TOPIC9=models.CharField(max_length=30);
    TOPIC10=models.CharField(max_length=30);
    
class trendingtopic(models.Model):    
    DATE=models.DateField();
    LOCATION=models.CharField(max_length=30);
    TOPIC1=models.CharField(max_length=30);
    TOPIC2=models.CharField(max_length=30);
    TOPIC3=models.CharField(max_length=30);
    TOPIC4=models.CharField(max_length=30);
    TOPIC5=models.CharField(max_length=30);
    TOPIC6=models.CharField(max_length=30);
    TOPIC7=models.CharField(max_length=30);
    TOPIC8=models.CharField(max_length=30);
    TOPIC9=models.CharField(max_length=30);
    TOPIC10=models.CharField(max_length=30);
    
    
class locationlist(models.Model):
    LOCATION=models.CharField(max_length=30);
    
class topiclist(models.Model):
    TOPIC=models.CharField(max_length=30);