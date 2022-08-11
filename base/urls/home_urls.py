from django.urls import path
from base.views import home_views as views


urlpatterns = [
    path('', views.gethome, name = 'home'),
]