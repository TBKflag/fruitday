from django import forms
from .models import *

class Cartform(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'
        labels = {
            'uphone':'手机号',
            'title':'商品',
            'price':'图片',
            'num':'数量',
            'pic':'价格',
        }
