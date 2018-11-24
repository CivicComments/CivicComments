from django.contrib.gis.db import models
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations
from django.contrib.postgres.fields import JSONField
import uuid
import settings
from django.contrib.auth.models import User

class Issue(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tags = JSONField(default=[])
    other_data = JSONField(default={})
    authored_by = models.ForeignKey(User, default=None, blank=True, null=True)
    parent_issue = models.ForeignKey('self', default=None, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.title, self.uuid)


class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue = models.ForeignKey(Issue)
    authored_by = models.ForeignKey(User, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', default=None, blank=True, null=True)
    short_summary = models.TextField(default='')
    content = models.TextField()
    tags = JSONField(default=[])
    is_approved = models.BooleanField(default=True)
    other_data = JSONField(default={})
