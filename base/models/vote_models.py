from django.db import models
from jsonfield import JSONField

# Models for Votes
class Vote(models.Model):
    proposalContractAddress = JSONField(null = True)
    proposalName = models.CharField(max_length=50)
    proposalUrl = JSONField(null = True)
    proposalSignature = JSONField(null = True)
    VoterSignature = JSONField(null = True)
    VoterChoice = JSONField(null = True)
    VoterAddress = JSONField(null = True)
    createdAt = JSONField(null = True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self._id)


       
