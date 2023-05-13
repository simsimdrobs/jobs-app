from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
# Create your views here.

def get(request):
    if request.method != 'GET':
        raise HttpResponseBadRequest
    return HttpResponse('jobs works!')