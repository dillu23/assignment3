# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
from django.utils.safestring import SafeString
from jsonwritegraph import jsonwritegraph
def sampleview(request):
    if request.method == 'GET':
        try:
            data=request.GET.get("cluster")
            r=int(data)
            if r==1:
                r=-1;
            handle=jsonwritegraph(r)
        except: 
            handle=jsonwritegraph(-1)
    fp = open('/Users/hp/git/assignment3/django1test/test1/templates/network.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({"nodes":SafeString(handle[0]),"edges":SafeString(handle[1])}))
    return HttpResponse(html)

def spanview(request):
    return HttpResponse("hi")
