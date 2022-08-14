from django.urls import path
from base.views import proposals_views as views


urlpatterns = [
    path('', views.getallproposals, name = 'all-proposals'),
    path('name', views.getproposalbyname, name = 'proposal-by-name'),
    path('type', views.getproposalbytype, name = 'proposal-by-type'),
    path('cid', views.getproposalbycid, name = 'proposal-by-cid'),
    path('identifier', views.getproposalbyidentifier, name = 'proposal-by-identifier'),
    path('creator', views.getproposalbycreator, name = 'proposal-by-creator'),
    path('category', views.getproposalbycategory, name = 'proposal-by-category'),
    path('daocid', views.getproposalbydaocid, name = 'proposal-by-daocid'),
    path('daoname', views.getproposalbydaoname, name = 'proposal-by-daoname'),
    path('set', views.setproposals, name = 'setproposals'),
]

