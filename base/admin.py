from django.contrib import admin
from .models.daos_models import *
from .models.proposals_models import *
from .models.vote_models import *


# Register your models here.

admin.site.register(Daos)
admin.site.register(Proposal)
admin.site.register(Vote)

