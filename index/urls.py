from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^login/', login_views,name='loginpage'),
    # url(r'^recv_login_inform/$',recv_views),
    url(r'^$', index_views, name='login'),
    url(r'^register/', register_views, name='register'),
    # url(r'^recv_register/$',recv_register),
]
