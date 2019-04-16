from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [         
    url(r'^admin/', admin.site.urls),
    url(r'', include('home.urls')),          
]
