from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(u'name',max_length=20)
    id_num = models.IntegerField(u'id_num')
    birth = models.DateField(u'birth')

class Test(models.Model):
    user = models.CharField(u'name',max_length=20)
    content = models.TextField(u'content')

class WebPage(models.Model):
    device_id = models.CharField(u'name',max_length=40)
    device_ip = models.CharField(u'device_ip',max_length=20)
    weburl = models.URLField(u'weburl',max_length=1000)
    page_content = models.TextField(u'page_content')

