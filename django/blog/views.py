from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    message = "Hello, World.  You're at the blog index."
    encoded_message = message.encode('utf-8')
    return HttpResponse(encoded_message)
