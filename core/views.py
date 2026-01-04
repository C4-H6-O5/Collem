from django.shortcuts import render
from django.http import HttpResponse
from .models import Asset

def home(request):
    assets = Asset.objects.all()

    content = "<h1> Welcome to Collem! </h1>"
    content += "<h3> Stored Files: </h3>"

    for asset in assets:
        content += f"<p>{asset.file.name}</p>"

    return HttpResponse(content)
