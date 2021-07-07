from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        # 특정한 user와 project 한 쌍이 이루는 Subscription은 오직 하나!
        unique_together = ('user', 'project')
