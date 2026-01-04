from django.shortcuts import render
from django.http import HttpResponse
from .models import Asset

def home(request):
    assets = Asset.objects.all()

    context = {'assets': assets}

    return render (request, 'core/home.html', context)
