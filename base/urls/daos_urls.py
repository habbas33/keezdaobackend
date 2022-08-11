from django.urls import path
from base.views import daos_views as views


urlpatterns = [
    path('data', views.getdaos, name = 'daos'),
    path('test', views.gettest, name = 'test'),
    path('set', views.setdaos, name = 'setdaos'),
]