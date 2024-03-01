import uuid as uuid
from django.db import models

# Create your models here.


class Article(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True, default="")

