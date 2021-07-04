from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    # 회원 탈퇴 시 작성자는 알 수 없음 등으로 표시
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    img = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
