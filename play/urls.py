from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from play.routers import router

admin.site.site_header = 'Game Administration'
admin.site.site_title = 'Game Administration'
admin.site.index_title = 'Game Administration'



urlpatterns = [
    path(
        '',
        TemplateView.as_view(
            template_name='index.html',
        ),
        name='index',
    ),

    path(
        'admin/', 
        admin.site.urls
    ),
    path(
        'api/v1/', 
        include(router.urls),
    ),
]
