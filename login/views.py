from django.shortcuts import render
from .models import SignupForm, LoginForm

# Create your views here.
def login_view(request):
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})