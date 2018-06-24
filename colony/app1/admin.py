# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import CreateProject, ProjectTag
# Register your models here.

admin.site.register(CreateProject)
admin.site.register(ProjectTag)
