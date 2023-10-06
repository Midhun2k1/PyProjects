from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

from . models import Place,Team



def demo(request):
    obj=Place.objects.all()
    act=Team.objects.all()
    return render(request,"index.html",{"result":obj,"actors":act})
# def about(request):
#     return render(request,"about1.html")
# def mim(request):
#     return HttpResponse("Hey this is multiple view bro")
# def passi(request):
#     return render(request,"passi.html")
# def addition(request):
#     x=int(request.GET["num1"])
#     y=int(request.GET["num2"])
#     res=x+y
#     return render(request,"result.html",{"result":res})