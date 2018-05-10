from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^login/', login_views,name='loginpage'),
    url(r'^$', index_views, name='login'),
    url(r'^register/', register_views, name='register'),
    url(r'^good_detail/(\d)*$',gooddetail_views,name='gooddetail'),
    url(r'^logout/$',logout_views),
    url(r'^addcart/(\d+)/$', addcart_views, name='cart'),
    url(r'^subcart/(\d+)/$', subcart_views,name='subcart'),
    url(r'^cart/$',cart_views,name='cart_view'),

]
