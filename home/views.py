from django.shortcuts import render
from django.http import HttpResponse
from .models import Skin

# Create your views here.
def index(request):

    skins = Skin.objects.all()

    return render(request, 'home/index.html', {
        "skins": skins
    })

