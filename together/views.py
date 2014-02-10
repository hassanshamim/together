from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<html><title>Together</title><h1>Together</h1><a href="/signup">Sign Up</a></html>')
