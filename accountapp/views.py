from django.shortcuts import render


def hello_world(request):
    return render(request, 'accountapp/helloworld.html')
    # alt+enter로 import 가능
