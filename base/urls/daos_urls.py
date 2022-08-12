from django.urls import path
from base.views import daos_views as views


urlpatterns = [
    path('', views.getalldaos, name = 'all-daos'),
    path('name', views.getdaobyname, name = 'dao-by-name'),
    path('cid', views.getdaobycid, name = 'dao-by-cid'),
    path('up', views.getdaobyup, name = 'dao-by-up'),
    path('creator', views.getdaobycreator, name = 'dao-by-creator'),
    path('category', views.getdaosbycategory, name = 'dao-by-category'),
    path('member', views.getdaosbymember, name = 'dao-by-member'),
    path('set', views.setdaos, name = 'setdaos'),
]

