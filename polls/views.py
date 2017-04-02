from django.shortcuts import render

# Create your views here.

def ir_index(request):
    return render(request,"polls/index.html")