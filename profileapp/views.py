from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
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
        temp_profile.user = self.request.user  # user 본인 데이터로 설정
        temp_profile.save()

        return super().form_valid(form)

    # 생성 후 디테일 페이지로 넘어가도록 수정
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})  # pk를 딕셔너리 형태로 kwargs로 넘기기


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
