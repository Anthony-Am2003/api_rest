import uuid
from django.db import models


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    is_activate = models.BooleanField(default=True)
