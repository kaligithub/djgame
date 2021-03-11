from django.contrib import admin
from django.urls import include, path

from play.routers import router

admin.site.site_header = 'Game Administration'
admin.site.site_title = 'Game Administration'
admin.site.index_title = 'Game Administration'



urlpatterns = [
    path(
        'admin/', 
        admin.site.urls
    ),
    path(
        'api/v1/', 
        include(router.urls),
    ),
]
