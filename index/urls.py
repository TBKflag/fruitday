from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^login/', login_views,name='loginpage'),
    url(r'^$', index_views, name='login'),
    url(r'^register/', register_views, name='register'),
]
