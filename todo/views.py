from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    people=[
        {"name":"ram","age":"2"},
        {"name":"shyam","age":"3"},
        {"name":"john","age":"4"},

        
    ]
    
    context={
        "people":people,
    }
    return render(request,"index.html",context)