from rest_framework import serializers

from base.models.daos_models import Daos

class DaosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daos
        # fields = ['_id', 'createdAt', 'daoName',  'description', 'profileImage']

        fields = ['_id', 'createdAt', 'daoName', 'profileImage', 'categories', 'description', 'keyPermissions', 'vaultDetails', 'votingParameters']
    # def get_reviews(self, obj):
    #     reviews = obj.review_set.all()
    #     serializer = ReviewSerializer(reviews, many=True)
    #     return serializer.data
# {
#     "daoName": "New Task",
#     "description": "daoName descripton"
#     "profileImage": {
#     "hash": "QmQHWFC1ewHiNR3kfTqMx7suN5CeR9UgsS2gF6k4Cbv2Ga",
#     "url": "https://ipfs.infura.io/ipfs/"
#     }
# }