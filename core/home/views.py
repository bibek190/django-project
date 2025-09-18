from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    
    peoples = [
        {"name":"bibek","age":24},
        {"name":"firoj","age":44},
        {"name":"hari","age":34},
        {"name":"prex","age":14},
    ]
    

    
    return render(request,"home/index.html",context = {"peoples":peoples})