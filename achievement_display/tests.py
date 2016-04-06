# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class IpWrite(models.Model):
    ip = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=100)

    class Meta:
        app_label = 'kankan'
        managed = False
        db_table = 'ip_write'


class Table(models.Model):
    ip = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField()

    class Meta:
        app_label = 'kankan'
        managed = False
        db_table = 'table'
