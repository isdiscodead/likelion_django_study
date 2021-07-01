from django.db import models


# Create your models here.

# 클래스 하나가 item 하나가 된다 !
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)  # 공백 X 문자열 필드
