from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render  # alt+enter로 import 가능
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        # create
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/helloworld.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    # CreateView에 필요한 주요 파라미터 지정
    model = User  # 장고 기본 Model, AbstractUser 클래스 이용 필드 추가 가능
    form_class = UserCreationForm
    success_url = reverse_lazy("accountapp:hello_world")  # reverse_lazy -> 클래스형, reverse -> 함수형
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    # 파라미터가 create와 거의 동일하다
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy("accountapp:hello_world")  # reverse_lazy -> 클래스형, reverse -> 함수형
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = 'accountapp/delete.html'
