from django.http import HttpResponse
from django.shortcuts import render
from .models import place, flower


# Create your views here.
def demo(request):
    obj = place.objects.all()
    obj1 = flower.objects.all()
    return render(request,'index.html',{'result':obj,'note':obj1})

    #return HttpResponse("heloooo")
# def about(request):
#      obj1=flower.objects.all()
#      return render(request,'index.html',{'note':obj1})

