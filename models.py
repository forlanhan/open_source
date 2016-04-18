# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Acmmetasource(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=64)  # Field name made lowercase.
    title = models.CharField(max_length=128, blank=True, null=True)
    detailpageid = models.CharField(db_column='detailPageId', max_length=24)  # Field name made lowercase.
    detailpageurl = models.CharField(db_column='detailPageUrl', max_length=256)  # Field name made lowercase.
    crawltime = models.DateTimeField(db_column='crawlTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACMMetaSource'


class Ieeemetasource(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=64)  # Field name made lowercase.
    title = models.CharField(max_length=128, blank=True, null=True)
    detailpageid = models.CharField(db_column='detailPageId', max_length=24)  # Field name made lowercase.
    detailpageurl = models.CharField(db_column='detailPageUrl', max_length=256)  # Field name made lowercase.
    crawltime = models.DateTimeField(db_column='crawlTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IEEEMetaSource'


class Wanfangmetasource(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=64)  # Field name made lowercase.
    title = models.CharField(max_length=128, blank=True, null=True)
    detailpageid = models.CharField(db_column='detailPageId', max_length=24)  # Field name made lowercase.
    detailpageurl = models.CharField(db_column='detailPageUrl', max_length=256)  # Field name made lowercase.
    crawltime = models.DateTimeField(db_column='crawlTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WanfangMetaSource'
