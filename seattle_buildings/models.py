from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.
class SeattleLandUsePermitDoc(models.Model):
    document_id = models.TextField(primary_key=True)
    name = models.TextField()
    url = models.TextField()
    land_use_id = models.TextField()
    date = models.DateField()
    is_text_machine_readable = models.NullBooleanField(blank=True, null=True, default=None)
    text = models.TextField(null=True, blank=True)
    structured_data = JSONField()
