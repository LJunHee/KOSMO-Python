from django.http import HttpResponse
from django.shortcuts import render


def intro(req):
    print('intro page...')
    # return HttpResponse('test page...')
    return render(req, 'intro.html')