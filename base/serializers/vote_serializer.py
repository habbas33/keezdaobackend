from rest_framework import serializers

from base.models.vote_models import Vote

class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['_id', 'createdAt', 'proposalContractAddress', 'proposalName', 'proposalName', 'proposalUrl', 'proposalSignature', 'VoterChoice', 'VoterAddress']

