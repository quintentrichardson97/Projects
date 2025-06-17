from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def artpage(request):

    return render(request, 'artistpage/artpage.html')