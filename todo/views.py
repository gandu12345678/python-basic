from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    people=[
        {"name":"ram","age":20},
        {"name":"shyam","age":30},
        {"name":"john","age":40},

        
    ]
    
    context={
        "people":people,
    }
    return render(request,"index.html",context)