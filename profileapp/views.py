from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    # 본인 프로필일 때 바꾸 수 있도록 !
    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # 임시 데이터 저장
        temp_profile.user = self.request.user   # user 본인 데이터로 설정
        temp_profile.save()

        return super().form_valid(form)