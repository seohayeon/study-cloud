from django.urls import path

from . import views
app_name = 'file' 

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('category/<str:category>', views.category, name='category'),
    path('<int:id>', views.info, name='info'),
]