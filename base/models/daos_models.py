from django.db import models
from jsonfield import JSONField
# from django.utils import timezone

# class CategoriesDicty(models.Model):
#     value = models.CharField(max_length=50)
#     label = models.CharField(max_length=50)

# class KeyPermissionsDicty(models.Model):
#     masterKey = models.BooleanField()
#     hrKey = models.BooleanField()
#     vote = models.BooleanField()
#     propose = models.BooleanField()
#     sendDelegate = models.BooleanField()
#     receiveDelegate = models.BooleanField()

# class PermissionsDicty(models.Model):
#     upAddress = models.CharField(max_length=42)
#     keyPermissions = models.ForeignKey(KeyPermissionsDicty, db_index=True, on_delete=models.CASCADE)

# class VaultDicty(models.Model):
#     vaultName = models.CharField(max_length=50)
#     majority = models.DecimalField(max_digits=2, decimal_places=2)
#     daoMembers = JSONField()

# class VotingDicty(models.Model):
#     participationRate = models.DecimalField(max_digits=2, decimal_places=2)
#     votingMajority = models.DecimalField(max_digits=2, decimal_places=2)
#     minVotingDelay = models.DecimalField(max_digits=4, decimal_places=0)
#     minVotingPeriod = models.DecimalField(max_digits=4, decimal_places=0)

# class ProfileImageDicty(models.Model):
#     profileImageHash = models.CharField(max_length=46)
#     profileImageUrl = models.CharField(max_length=50)
    


# Models for daos
class Daos(models.Model):
    daoName = models.CharField(max_length=50)
    profileImage = JSONField(null = True)
    categories = JSONField(null = True)
    description = models.TextField( null = False)
    keyPermissions = JSONField(null = True)
    vaultDetails = JSONField(null = True)
    votingParameters = JSONField(null = True)

    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self._id)