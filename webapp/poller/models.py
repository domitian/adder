from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Job(models.Model):
    QUEUED = 0
    FINISHED = 1
    STATUS_OPTIONS = (
            (QUEUED,'Queued'),
            (FINISHED,'Finished'),
            )
    status = models.IntegerField(choices=STATUS_OPTIONS,default=QUEUED)
    inp = models.CharField(max_length=200)
    result = models.CharField(max_length=200)

