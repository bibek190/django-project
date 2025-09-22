from django.shortcuts import render,redirect

from .models import *

# Create your views here.
def vege(request):
    
    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")

        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_description = receipe_description,
            receipe_name = receipe_name
        )
        return redirect("/receipes/")
    
    return render(request,"vege.html")