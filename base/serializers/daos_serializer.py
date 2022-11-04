from rest_framework import serializers

from base.models.daos_models import Daos

class DaosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daos
        fields = ['_id', 'createdAt', 'daoName', 'profileImage', 'categories', 'description', 'daoLink', 'keyPermissions', 'vaultDetails', 'votingParameters', 'daoUpAddress', 'creator', 'url', 'CID']
