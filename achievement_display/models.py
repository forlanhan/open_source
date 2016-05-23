# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Baidumetasource(models.Model):
    wkid = models.AutoField(db_column='WKID', primary_key=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', unique=True, max_length=36)  # Field name made lowercase.
    originalurl = models.CharField(db_column='originalUrl', max_length=200)  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=200)  # Field name made lowercase.
    storeloc = models.CharField(db_column='storeLoc', max_length=500)  # Field name made lowercase.
    crawltime = models.DateTimeField(db_column='crawlTime')  # Field name made lowercase.
    fileabstract = models.CharField(db_column='fileAbstract', max_length=2000)  # Field name made lowercase.
    filetype = models.CharField(db_column='fileType', max_length=50)  # Field name made lowercase.
    filecategory = models.CharField(db_column='fileCategory', max_length=100)  # Field name made lowercase.
    fileauthor = models.CharField(db_column='fileAuthor', max_length=50)  # Field name made lowercase.
    downloadcount = models.IntegerField(db_column='downloadCount')  # Field name made lowercase.
    readcount = models.IntegerField(db_column='readCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BaiduMetaSource'


class Docbmcheckresult(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    processtime = models.DateTimeField(db_column='processTime')  # Field name made lowercase.
    processresult = models.IntegerField(db_column='processResult')  # Field name made lowercase.
    alertnum = models.IntegerField(db_column='alertNum')  # Field name made lowercase.
    score = models.IntegerField()
    reserverint = models.IntegerField(db_column='reserverInt', blank=True, null=True)  # Field name made lowercase.
    reserverstr = models.CharField(db_column='reserverStr', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DocBMCheckResult'


class Docinfo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    docstoragepath = models.CharField(db_column='docStoragePath', max_length=1024)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DocInfo'


class Docyxcheckresult(models.Model):
    tid = models.AutoField(db_column='TID', primary_key=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', unique=True, max_length=36)  # Field name made lowercase.
    processtime = models.DateTimeField(db_column='processTime')  # Field name made lowercase.
    checkstat = models.IntegerField(db_column='checkStat')  # Field name made lowercase.
    picnum = models.IntegerField(db_column='picNum')  # Field name made lowercase.
    alertpicnum = models.IntegerField(db_column='alertPicNum')  # Field name made lowercase.
    pidlist = models.CharField(db_column='PIDList', max_length=2048, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DocYXCheckResult'


class Hiddenfileinfo(models.Model):
    hiddenfileid = models.AutoField(db_column='hiddenFileID', primary_key=True)  # Field name made lowercase.
    hiddenfilesrcname = models.CharField(db_column='hiddenFileSrcName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    hiddenfilestoragename = models.CharField(db_column='hiddenFileStorageName', max_length=128)  # Field name made lowercase.
    hiddenfilelen = models.IntegerField(db_column='hiddenFileLen')  # Field name made lowercase.
    hiddenfilestoragepath = models.CharField(db_column='hiddenFileStoragePath', max_length=1024)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HiddenFileInfo'


class Picyxcheckresult(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=36)  # Field name made lowercase.
    processtime = models.DateTimeField(db_column='processTime')  # Field name made lowercase.
    picname = models.CharField(db_column='picName', max_length=64)  # Field name made lowercase.
    pictype = models.CharField(db_column='picType', max_length=16)  # Field name made lowercase.
    picstoragepath = models.CharField(db_column='picStoragePath', max_length=1024)  # Field name made lowercase.
    hiddensoft = models.CharField(db_column='hiddenSoft', max_length=128, blank=True, null=True)  # Field name made lowercase.
    hiddenfileidlist = models.CharField(db_column='hiddenFileIDList', max_length=512, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PicYXCheckResult'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Tmpbaidumetasource(models.Model):
    wkid = models.AutoField(db_column='WKID', primary_key=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', unique=True, max_length=36)  # Field name made lowercase.
    originalurl = models.CharField(db_column='originalUrl', max_length=200)  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=200)  # Field name made lowercase.
    storeloc = models.CharField(db_column='storeLoc', max_length=500)  # Field name made lowercase.
    crawltime = models.DateTimeField(db_column='crawlTime')  # Field name made lowercase.
    fileabstract = models.CharField(db_column='fileAbstract', max_length=2000)  # Field name made lowercase.
    filetype = models.CharField(db_column='fileType', max_length=50)  # Field name made lowercase.
    filecategory = models.CharField(db_column='fileCategory', max_length=100)  # Field name made lowercase.
    fileauthor = models.CharField(db_column='fileAuthor', max_length=50)  # Field name made lowercase.
    downloadcount = models.IntegerField(db_column='downloadCount')  # Field name made lowercase.
    readcount = models.IntegerField(db_column='readCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpBaiduMetaSource'


class Acmmetasource(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=64)  # Field name made lowercase.
    title = models.CharField(max_length=128, blank=True, null=True)
    detailpageid = models.CharField(db_column='detailPageId', max_length=24)  # Field name made lowercase.
    detailpageurl = models.CharField(db_column='detailPageUrl', max_length=256)  # Field name made lowercase.
    crawltime = models.DateTimeField(db_column='crawlTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACMMetaSource'


class Cnkimetasource(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=64)  # Field name made lowercase.
    title = models.CharField(max_length=128, blank=True, null=True)
    detailpageid = models.CharField(db_column='detailPageId', max_length=24)  # Field name made lowercase.
    detailpageurl = models.CharField(db_column='detailPageUrl', max_length=256)  # Field name made lowercase.
    crawltime = models.DateTimeField(db_column='crawlTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CNKIMetaSource'


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
