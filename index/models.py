from django.db import models

# Create your models here.


class Users(models.Model):
    uphone = models.CharField(max_length=20)
    upwd = models.CharField(max_length=30)
    uemail = models.EmailField()
    uname = models.CharField(max_length=30)
    isActive = models.BooleanField(default=True)


class GoodsType(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    picture = models.ImageField(upload_to='static/upload/goodstype')


class Goods(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    spec = models.CharField(max_length=30)
    picture=models.ImageField(upload_to='static/upload/goods')
    isActive=models.BooleanField(default=True)
