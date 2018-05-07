from django.contrib import admin
from .models import *
# Register your models here.
class bannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'picture']

class GoodAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'price', 'spec', 'picture', 'isActive']
    list_editable=['title','price','spec','picture','isActive']
    search_fields=['title','spec']
    list_filter=['price']

class userAdmin(admin.ModelAdmin):
    list_display = ['id','uname', 'uphone', 'uemail', 'isActive']
    list_editable = ['uname','uphone', 'uemail', 'isActive']
    search_fields=['uname','uphone','uemail']
    fields=['uname','uphone','uemail','isActive']

class goodtypeAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'desc', 'picture']
    list_editable = ['title','desc', 'picture']


admin.site.register(Users, userAdmin)
admin.site.register(GoodsType, goodtypeAdmin)
admin.site.register(Goods, GoodAdmin)
admin.site.register(Banner,bannerAdmin)
admin.site.register(SmallBanner)
