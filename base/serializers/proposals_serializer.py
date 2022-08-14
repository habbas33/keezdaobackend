from rest_framework import serializers

from base.models.proposals_models import Proposal

class ProposalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['_id', 'createdAt', 'proposalType', 'proposalName', 'categories', 'description', 'proposalDetails', 'forDaoDetails', 'identifier', 'creator', 'url', 'CID']
