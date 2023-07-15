from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def topic_insertion(request):
    TMFO=TopicForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFOD=TopicForm(request.POST)
        if TMFOD.is_valid():
            TMFOD.save()
            return HttpResponse('the topic data is inserted successfully')
        else:
            return HttpResponse('error')
    

    return render(request,'topic_insertion.html',context=d)
def webpage_insertion(request):
    WMFO=WebpageForm()
    d={'WMFO':WMFO}
    if request.method=='POST':
        WMFOD=WebpageForm(request.POST)
        if WMFOD.is_valid():
            WMFOD.save()
            return HttpResponse('the webpage data is inserted successfully')
        else:
            return HttpResponse('error')

    return render(request,'webpage_insertion.html',context=d)

def accessrecord_insertion(request):
    AMFO=AccessrecordForm()
    d={'AMFO':AMFO}
    if request.method=='POST':
        AMFOD=AccessrecordForm(request.POST)
        if AMFOD.is_valid():
            AMFOD.save()
            return HttpResponse('the accessrecord data is inserted successfully')
        else:
            return HttpResponse('Error')
    return render(request,'accessrecord_insertion.html',context=d)


