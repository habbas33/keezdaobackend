from django.db import models
from jsonfield import JSONField

# Models for proposals
class Proposal(models.Model):
    proposalType = models.CharField(max_length=50)
    proposalName = models.CharField(max_length=50)
    categories = JSONField(null = True)
    description = models.TextField( null = False)
    proposalDetails = JSONField(null = True)
    forDaoDetails = JSONField(null = True)
    CID = JSONField(null = True)
    url = JSONField(null = True)
    creator = JSONField(null = True)
    identifier = JSONField(null = True)

    createdAt = JSONField(null = True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self._id)

