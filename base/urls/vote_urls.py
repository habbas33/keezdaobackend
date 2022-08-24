from django.urls import path
from base.views import vote_views as views


urlpatterns = [
    path('', views.getallvotes, name = 'all-votes'),
    path('signature', views.getvotesbyproposalsignature, name = 'votes-by-proposal-signature'),
    path('url', views.getvotesbyproposalurl, name = 'votes-by-proposal-url'),
    # path('cid', views.getvotesbyproposalcid, name = 'votes-by-proposal-cid'),
    path('voter', views.getvotesbyvoter, name = 'votes-by-voter'),
    path('set', views.setvote, name = 'setvote'),
]

