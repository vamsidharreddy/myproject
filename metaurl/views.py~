# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import metadata,metadataform
import urllib2,re

def showform(request):
    
    return render_to_response('showform.html',context_instance=RequestContext(request))
    
def getdata(request):
    print request.method
    if request.method=='GET':
       url=request.GET.get('url')
       try:
          m=metadata.objects.get(pk=url)
          m1=metadataform(instance=m)
       except:   
          response=urllib2.urlopen(url)
          st=response.read()
          m1=re.compile('<meta name="description" content="(.*?)."', re.DOTALL).search(st)
          m2=re.compile('<meta name="keywords" content="(.*?)"',re.DOTALL).search(st)
          m3=re.compile('<title.*?>(.*?)</title>',re.DOTALL).search(st)
          m=metadata()
          m.url=url
          try:
            m.title=m3.group(1)
          except:
            pass
          try:
            m.meta_desc=m1.group(1)
          except:
            pass
          try:
            m.meta_keyw=m2.group(1)
          except:
           pass
          m.save()
          m1=metadataform(instance=m)
       return render_to_response('showdata.html',{'m':m1},context_instance=RequestContext(request))
    else:
       k=metadata.objects.get(pk=request.POST.get('url'))
       m=metadataform(request.POST,instance=k)
       if m.is_valid():
          m.save()
          
       return render_to_response('showdata.html',{'m':m},context_instance=RequestContext(request))
    
          
    
        
