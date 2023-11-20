from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lokesh(request):
    data='jinja tags is a high level operations for creating the semi-dynamic applications'
    d={'chatta':data}
    return render(request,'lokesh.html',context=d)


def kumar(request):
    a='Am kumar.My best buddy is loki bai'
    d={'loki':a}
    return render(request,'kumar.html',d)
