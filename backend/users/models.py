from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """ 用户模型 """
    email = models.EmailField(unique=True, verbose_name='邮箱')
    phone = models.CharField(max_length=20, blank=True, verbose_name='手机号')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='生日')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='头像')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')