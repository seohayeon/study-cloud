from django.contrib import admin
from django.urls import path,include
from file import views

urlpatterns = [
    path('', views.index),
    path('upload/', include('upload.urls')),
    path('file/', include('file.urls')),
    path('admin/', admin.site.urls),
]
