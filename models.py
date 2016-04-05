# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AchievementDisplayPerson(models.Model):
    kaoshenghao = models.CharField(max_length=150, blank=True, null=True)
    shenfenzhenghao = models.CharField(max_length=150, blank=True, null=True)
    xingming = models.CharField(max_length=150, blank=True, null=True)
    xingbiedaima = models.CharField(max_length=150, blank=True, null=True)
    xingbie = models.CharField(max_length=150, blank=True, null=True)
    minzudaima = models.CharField(max_length=150, blank=True, null=True)
    minzu = models.CharField(max_length=150, blank=True, null=True)
    zhengzhimianmaodaima = models.CharField(max_length=150, blank=True, null=True)
    zhengzhimianmao = models.CharField(max_length=150, blank=True, null=True)
    yuanxiaodaima = models.CharField(max_length=150, blank=True, null=True)
    yuanxiaomingcheng = models.CharField(max_length=150, blank=True, null=True)
    fenxiaomingcheng = models.CharField(max_length=150, blank=True, null=True)
    xuelidaima = models.CharField(max_length=150, blank=True, null=True)
    xueli = models.CharField(max_length=150, blank=True, null=True)
    zhuanyedaima = models.CharField(max_length=150, blank=True, null=True)
    zhuanye = models.CharField(max_length=150, blank=True, null=True)
    zhuanyefangxiang = models.CharField(max_length=150, blank=True, null=True)
    peiyangfangshidaima = models.CharField(max_length=150, blank=True, null=True)
    peiyangfangshi = models.CharField(max_length=150, blank=True, null=True)
    dingxianghuoweipeidanwei = models.CharField(max_length=150, blank=True, null=True)
    shengyuansuozaididaima = models.CharField(max_length=150, blank=True, null=True)
    shengyuansuozaidi = models.CharField(max_length=150, blank=True, null=True)
    chengxiangshengyuan = models.CharField(max_length=150, blank=True, null=True)
    xuezhi = models.CharField(max_length=150, blank=True, null=True)
    ruxueshijian = models.CharField(max_length=150, blank=True, null=True)
    biyeshijian = models.CharField(max_length=150, blank=True, null=True)
    shifanshengleibiedaima = models.CharField(max_length=150, blank=True, null=True)
    shifanshengleibie = models.CharField(max_length=150, blank=True, null=True)
    kunnanshengleibiedaima = models.CharField(max_length=150, blank=True, null=True)
    kunnanshengleibie = models.CharField(max_length=150, blank=True, null=True)
    suozaiyuanxi = models.CharField(max_length=150, blank=True, null=True)
    suozaibanji = models.CharField(max_length=150, blank=True, null=True)
    xuehao = models.CharField(max_length=150, blank=True, null=True)
    chushengriqi = models.CharField(max_length=150, blank=True, null=True)
    shoujihaoma = models.CharField(max_length=150, blank=True, null=True)
    biyequxiangdaima = models.CharField(max_length=150, blank=True, null=True)
    biyequxiang = models.CharField(max_length=150, blank=True, null=True)
    danweizuzhijigoudaima = models.CharField(max_length=150, blank=True, null=True)
    danweimingcheng = models.CharField(max_length=150, blank=True, null=True)
    danweixingzhidaima = models.CharField(max_length=150, blank=True, null=True)
    danweixingzhi = models.CharField(max_length=150, blank=True, null=True)
    danweihangyedaima = models.CharField(max_length=150, blank=True, null=True)
    danweihangye = models.CharField(max_length=150, blank=True, null=True)
    danweisuozaididaima = models.CharField(max_length=150, blank=True, null=True)
    danweisuozaidi = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'achievement_display_person'


class AchievementDisplayTest(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'achievement_display_test'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Form(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'form'


class Jobcount(models.Model):
    zhuangtai = models.CharField(max_length=30)
    zhuanyemingcheng = models.CharField(max_length=100)
    kaoshenghao = models.CharField(max_length=100)
    xingming = models.CharField(max_length=50)
    xingbie = models.CharField(max_length=30)
    banji = models.CharField(max_length=100)
    shengfenzhenhao = models.CharField(max_length=200)
    xuezhi = models.CharField(max_length=30)
    xueli = models.CharField(max_length=30)
    xuehao = models.CharField(max_length=100, blank=True, null=True)
    danweixingzhi = models.CharField(max_length=100)
    danweimingcheng = models.CharField(max_length=100)
    danweisuozaidi = models.CharField(max_length=100)
    peiyangfangshi = models.CharField(max_length=100)
    shengyuandi = models.CharField(max_length=100)
    shifouzhuce = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'jobcount'


class Table1(models.Model):
    time = models.DateTimeField()
    p816sv = models.FloatField(db_column='P816SV')  # Field name made lowercase.
    p816mv = models.FloatField(db_column='P816MV')  # Field name made lowercase.
    p816pv = models.FloatField(db_column='P816PV')  # Field name made lowercase.
    s802k1sv = models.FloatField(db_column='S802K1SV')  # Field name made lowercase.
    s802k1mv = models.FloatField(db_column='S802K1MV')  # Field name made lowercase.
    s802k1pv = models.FloatField(db_column='S802K1PV')  # Field name made lowercase.
    s802k2sv = models.FloatField(db_column='S802K2SV')  # Field name made lowercase.
    s802k2mv = models.FloatField(db_column='S802K2MV')  # Field name made lowercase.
    s802k2pv = models.FloatField(db_column='S802K2PV')  # Field name made lowercase.
    s803k1sv = models.FloatField(db_column='S803K1SV')  # Field name made lowercase.
    s803k1mv = models.FloatField(db_column='S803K1MV')  # Field name made lowercase.
    s803k1pv = models.FloatField(db_column='S803K1PV')  # Field name made lowercase.
    s803k2sv = models.FloatField(db_column='S803K2SV')  # Field name made lowercase.
    s803k2mv = models.FloatField(db_column='S803K2MV')  # Field name made lowercase.
    s803k2pv = models.FloatField(db_column='S803K2PV')  # Field name made lowercase.
    s803k3sv = models.FloatField(db_column='S803K3SV')  # Field name made lowercase.
    s803k3mv = models.FloatField(db_column='S803K3MV')  # Field name made lowercase.
    s803k3pv = models.FloatField(db_column='S803K3PV')  # Field name made lowercase.
    s803k4sv = models.FloatField(db_column='S803K4SV')  # Field name made lowercase.
    s803k4mv = models.FloatField(db_column='S803K4MV')  # Field name made lowercase.
    s803k4pv = models.FloatField(db_column='S803K4PV')  # Field name made lowercase.
    g870ksv = models.FloatField(db_column='G870KSV')  # Field name made lowercase.
    g870kmv = models.FloatField(db_column='G870KMV')  # Field name made lowercase.
    g870kpv = models.FloatField(db_column='G870KPV')  # Field name made lowercase.
    d870kppv = models.FloatField(db_column='D870KPPV')  # Field name made lowercase.
    d870kpsv = models.FloatField(db_column='D870KPSV')  # Field name made lowercase.
    d870ktsv = models.FloatField(db_column='D870KTSV')  # Field name made lowercase.
    d870ktpv = models.FloatField(db_column='D870KTPV')  # Field name made lowercase.
    d870ktxv = models.IntegerField(db_column='D870KTXV')  # Field name made lowercase.
    g871ksv = models.FloatField(db_column='G871KSV')  # Field name made lowercase.
    g871kmv = models.FloatField(db_column='G871KMV')  # Field name made lowercase.
    g871kpv = models.FloatField(db_column='G871KPV')  # Field name made lowercase.
    p826ktsv = models.FloatField(db_column='P826KTSV')  # Field name made lowercase.
    p826ktmv = models.FloatField(db_column='P826KTMV')  # Field name made lowercase.
    p826ktpv = models.FloatField(db_column='P826KTPV')  # Field name made lowercase.
    p826knsv = models.FloatField(db_column='P826KNSV')  # Field name made lowercase.
    p826knmv = models.FloatField(db_column='P826KNMV')  # Field name made lowercase.
    p826knpv = models.FloatField(db_column='P826KNPV')  # Field name made lowercase.
    s804k = models.IntegerField(db_column='S804K')  # Field name made lowercase.
    p816kxv = models.IntegerField(db_column='P816KXV')  # Field name made lowercase.
    s802k1xv = models.IntegerField(db_column='S802K1XV')  # Field name made lowercase.
    s802k2xv = models.IntegerField(db_column='S802K2XV')  # Field name made lowercase.
    s803k1xv = models.IntegerField(db_column='S803K1XV')  # Field name made lowercase.
    s803k2xv = models.IntegerField(db_column='S803K2XV')  # Field name made lowercase.
    s803k3xv = models.IntegerField(db_column='S803K3XV')  # Field name made lowercase.
    s803k4xv = models.IntegerField(db_column='S803K4XV')  # Field name made lowercase.
    dld = models.IntegerField(db_column='DLD')  # Field name made lowercase.
    stop = models.IntegerField(db_column='STOP')  # Field name made lowercase.
    low = models.IntegerField(db_column='LOW')  # Field name made lowercase.
    high = models.IntegerField(db_column='HIGH')  # Field name made lowercase.
    heat = models.IntegerField(db_column='HEAT')  # Field name made lowercase.
    g808kxv = models.IntegerField(db_column='G808KXV')  # Field name made lowercase.
    g813kxv = models.IntegerField(db_column='G813KXV')  # Field name made lowercase.
    g814kxv = models.IntegerField(db_column='G814KXV')  # Field name made lowercase.
    p871k = models.IntegerField(db_column='P871K')  # Field name made lowercase.
    p870k = models.IntegerField(db_column='P870K')  # Field name made lowercase.
    p824xv = models.IntegerField(db_column='P824XV')  # Field name made lowercase.
    g806kxv = models.IntegerField(db_column='G806KXV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table1'
