from django.shortcuts import render,HttpResponse,redirect
from .models import Task
# Create your views here.
def index(request):

    tasks=Task.objects.all()
    context={
        
        "tasks":tasks
    }
    return render(request,"index.html",context)

def contact(request):
    return render (request,"contact.html")

def create(request):
    if request.method =="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        Task.objects.create(name=name,description=description)
        return redirect("/")

    return render(request,"create.html") 