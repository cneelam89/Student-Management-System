from django.shortcuts import render,HttpResponseRedirect
from .models import Student
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def show (request):
    std=Student.objects.all()
    return render (request, "crudapp/show.html",{'std':std})

def createdata(request):
    if request.method == "POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fn=fm.cleaned_data["fname"]
            ln=fm.cleaned_data["lname"]
            en=fm.cleaned_data["email"]
            print(fm.cleaned_data)
            reg=Student(fname=fn,lname=ln,email=en)
            messages.info(request, 'Saved !!!')
            reg.save()
            return HttpResponseRedirect("/")
    else:
        fm=StudentRegistration()
    return render (request,"crudapp/create.html",{'form':fm})

def updatedata(request ,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/")
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render (request, "crudapp/update.html",{'fm':fm})
   

def deletedata(request ,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")
