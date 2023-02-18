from django.shortcuts import HttpResponse
from django.shortcuts import render
from.models import place
from.models import name



def demo(request):
     # obj=place.objects.all()
     obj= name.objects.all()
     return render(request,"index.html",{'result':obj})

# def addition(request):
#      x=int(request.GET['num1'])
#      y=int(request.GET['num2'])
#      res=x+y
#      return render(request,"result.html",{'result':res})
