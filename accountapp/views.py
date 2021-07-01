from django.shortcuts import render # alt+enter로 import 가능


def hello_world(request):

    if request.method == "POST":
        return render(request, 'accountapp/helloworld.html', context={'text':'POST METHOD!'})
    else:
        return render(request, 'accountapp/helloworld.html', context={'text': 'GET METHOD!'})
