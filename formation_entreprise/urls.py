from django.contrib import admin
from django.urls import path, include
from formations.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', home, name='home'),
    path('', include('comptes.urls')),
    path('', include('formations.urls')),
]