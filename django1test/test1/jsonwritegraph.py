def jsonwritegraph(cluster):
    from test1.models import r1_nodes,r1_edges,Nodes,Edges
    from django.db.models import Sum
    import json
    x=int(cluster)
    if x==-1:
        nodes=r1_nodes.objects.all()
        edges=r1_edges.objects.all()
    else:
        nodes=Nodes.objects.filter(LABEL2=x)
        edges=Edges.objects.filter(LABEL1=x)
    
    handle=[""]*2
    
    
    count=nodes.count()
    arr=[""]*count
    
    i=0
    
    if x==-1:
        wt=int(edges.order_by("WEIGHT")[0].WEIGHT)
    else:
        wt=1
    for node in nodes:
            list1={}
            if x==-1:
                list1["name"]="0."+str(node.LABEL1)+"."+str(node.LABEL2)+"."+str(node.LABEL3)
            else:
                list1["name"]=str(x)+"."+str(node.LABEL3)+"."+str(node.LABEL4)+"."+str(node.LABEL5)+"."+str(node.LABEL)+"."+str(node.ID)
            list1["size"]=node.SIZE
            arr[i]=list1
            i=i+1
            
    handle[0]=json.dumps(arr)        
    
    count=edges.count()
    arr=[""]*count
    i=0
    for edge in edges:
        list1={}
        node=nodes.get(ID=edge.SOURCE)
        if x==-1:
            list1["source"]="0."+str(node.LABEL1)+"."+str(node.LABEL2)+"."+str(node.LABEL3)
        else:
            list1["source"]=str(x)+"."+str(node.LABEL3)+"."+str(node.LABEL4)+"."+str(node.LABEL5)+"."+str(node.LABEL)+"."+str(node.ID)
        node=nodes.get(ID=edge.TARGET)
        if x==-1:
            list1["target"]="0."+str(node.LABEL1)+"."+str(node.LABEL2)+"."+str(node.LABEL3)
            list1["weight"]=int(int(edge.WEIGHT)*20/wt)
        else:
            list1["target"]=str(x)+"."+str(node.LABEL3)+"."+str(node.LABEL4)+"."+str(node.LABEL5)+"."+str(node.LABEL)+"."+str(node.ID)
            list1["weight"]=int(1*20/wt)
        
        arr[i]=list1
        i=i+1
        
    handle[1]=json.dumps(arr)
    return handle

def jsonwritespan(topic):
    from test1.models import r1_nodes,r1_edges
    nodes=r1_nodes.objects.all()
    count=nodes.count()
    for node in nodes:
        list1={}
        list1["name"]="0."+str(node.LABEL1)+"."+str(node.LABEL2)+"."+str(node.LABEL3)