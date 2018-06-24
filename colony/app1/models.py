# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CreateProject(models.Model):

    project_title = models.CharField(max_length=100, null=True, blank=True)
    domainId = models.CharField(max_length=5, null=True, blank=True)
    project_brief = models.TextField(null=True, blank=True)
    creator_address = models.CharField(max_length=100, null=True, blank=True)
    creator_name = models.CharField(max_length=100, null=True, blank=True)
    txn_hash = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):

        return self.project_title


class ProjectTag(models.Model):

    tag = models.CharField(max_length=100, null=True, blank=True)
    tag_body = models.TextField(null=True, blank=True)

    def __unicode__(self):

        return self.tag