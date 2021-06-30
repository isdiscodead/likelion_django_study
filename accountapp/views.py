from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse('Hello world!')  # alt+enter로 import 가능
