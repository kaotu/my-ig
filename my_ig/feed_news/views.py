from django.http import HttpResponse
from django.shortcuts import render


def myfeed_views(request):
    return HttpResponse("Hello, World")
