from django.shortcuts import render
from .models import UploadFile


def index(request):
    if request.method != "POST":
        return render(request,'index.html',{})
    for x in request.FILES.getlist("files"):
        file = UploadFile(file=x)
        if file.file.size > 20971520:
            return render(request, "index.html",
                          {"error": "Please keep file size under {}.".format("20MB")})
        file.save()
    return render(request, "index.html")
