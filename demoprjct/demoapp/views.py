from django.http import HttpResponse
from django.shortcuts import render
#from multiplemodelssingleview.models import place,people
from . models import place
from . models import leads

# Create your views here.
def index(request):
    obj = place.objects.all()
    people = leads.objects.all()
    return render(request,'index.html',{'result':obj, 'leads':people})



#def helloworld(request):
#   return render(request,"home.html")
#def about(request):
#    return render(request,'about.html')
#def form(request):
 #   return render(request,'form.html')
##def result(request):
 #   num1 = int(request.GET['num1'])
 #   num2 = int(request.GET['num2'])
 #   add = num1 + num2
 #   sub = num1 - num2
 #   mul = num1 * num2
 #   div = num1 / num2

 #   return render(request,'result.html',{"num1":num1,"num2":num2,"add":add,"sub":sub,"mul":mul,"div":div})



