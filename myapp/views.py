from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    imageslider = ImageSliderModel.objects.all()
    context = {
        'imageslider': imageslider
    }
    return render(request, 'index.html', context)