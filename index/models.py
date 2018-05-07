from django.db import models

# Create your models here.

class Banner(models.Model):
    title=models.CharField(max_length=30,verbose_name='banner')
    picture=models.ImageField(upload_to='staic/upload/banner',verbose_name='图片')
    def __str__(self):
        return self.title

class Users(models.Model):
    uphone = models.CharField(max_length=20,verbose_name='电话号码')
    upwd = models.CharField(max_length=30,verbose_name='密码')
    uemail = models.EmailField(verbose_name='邮箱')
    uname = models.CharField(max_length=30,verbose_name='用户名')
    isActive = models.BooleanField(default=True, verbose_name='启用')
    def __str__(self):
        return self.uname
    class Meta:
        db_table = 'users'
        verbose_name='用户'
        verbose_name_plural=verbose_name

class GoodsType(models.Model):
    title = models.CharField(max_length=30, verbose_name='类别')
    desc = models.TextField(verbose_name='描述')
    picture = models.ImageField(
        upload_to='static/upload/goodstype', verbose_name='图片')
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'goodsytpe'
        verbose_name='商品类别'
        verbose_name_plural=verbose_name


class Goods(models.Model):
    title = models.CharField(max_length=30,verbose_name='商品类别')
    price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='价格')
    spec = models.CharField(max_length=30,verbose_name='介绍')
    picture=models.ImageField(upload_to='static/upload/goods',verbose_name='图片')
    isActive = models.BooleanField(default=True, verbose_name='启用')
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'goods'
        verbose_name='商品'
        verbose_name_plural=verbose_name

