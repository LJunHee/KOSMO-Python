from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'home/index.html')

def intro(req):
    return render(req, 'home/intro.html')