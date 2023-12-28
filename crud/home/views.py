from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.models import family
# Create your views here.
def home(request):
    return render(request,"home.html")


def show(request):
    data=family.objects.all()
    return render(request,'show.html',{'data':data})

def send(request):
    if request.method=='POST':
        Id=request.POST['id']
        Name=request.POST['Name']
        Surname=request.POST['Surname']
        Age=request.POST['Age']
        family(Id=Id,Name=Name,Surname=Surname,Age=Age).save()
        msg="Data Store Successfully ..."
        return render(request,"home.html",{'msg':msg})


    else:
        return HttpResponse("<h1>$)$ - Not Found </h1>")
    

def delete(request):
    Id=request.GET['Id']
    family.objects.filter(Id=Id).delete()
    return HttpResponseRedirect("show")

def edit(request):
    Id=request.GET['Id']
    Name=Surname=Age="not available"
    for data in  family.objects.filter(Id=Id):
        Name=data.Name
        Surname=data.Surname
        Age=data.Age
    return render(request,"edit.html",{'Id':Id,'Name':Name,'Surname':Surname,'Age':Age})

def recordedit(request):
    if request.method == 'POST':
        Id=request.POST['id']
        Name=request.POST['Name']
        Surname=request.POST['Surname']
        Age=request.POST['Age']
        family.objects.filter(Id=Id).update(Name=Name,Surname=Surname,Age=Age)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

