# rolchoise port, admin, reader, publisher
from django.db import models


class RoleChoice(models.TextChoices):
    ADMIN = ('Admin', 'admin')
    READER = ('Reader', 'reader')
    PUBLISHER = ('Publisher', 'publisher')