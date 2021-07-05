from django.urls import path

from commentapp.views import CommentCreateView

# 앱 이름 명시하기
app_name = "commentapp"

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
]
