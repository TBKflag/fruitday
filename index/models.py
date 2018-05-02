from django.db import models

# Create your models here.


class Users(models.Model):
    uphone = models.Charfield(max_length=20)
    upwd = models.CharField(max_length=30)
    uemail = models.EmailField()
    uname = models.CharField(max_length=30)
    isActive = models.BooleanField(default=True)


class GoodsType(models.Model):
    title = ''
    picture = 'static/upload/goodtype'
    desc =


class Goods(models.Model):
    title =
    price =
    spec =
