from django.db import models
from jsonfield import JSONField

# Models for daos
class Daos(models.Model):
    daoName = models.CharField(max_length=50)
    profileImage = JSONField(null = True)
    categories = JSONField(null = True)
    description = models.TextField( null = False)
    keyPermissions = JSONField(null = True)
    vaultDetails = JSONField(null = True)
    votingParameters = JSONField(null = True)
    votingParameters = JSONField(null = True)
    CID = JSONField(null = True)
    url = JSONField(null = True)
    creator = JSONField(null = True)
    daoUpAddress = JSONField(null = True)

    createdAt = JSONField(null = True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self._id)

