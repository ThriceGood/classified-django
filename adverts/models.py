from django.db import models
from django.contrib.auth.models import User
from time import time


def get_upload_file_name(instance, filename):
    return '%s_%s' % (str(time()).replace('.','_'), filename)


class Advert(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey('Category', null=False)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    price = models.IntegerField(null=False)
    image = models.FileField(upload_to=get_upload_file_name, null=True, blank=True)
    location = models.CharField(max_length=50, null=False)
    pub_date = models.DateField(auto_now_add=True)


class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category


class Comment(models.Model):
    user = models.ForeignKey(User)
    advert = models.ForeignKey('Advert')
    text = models.TextField(null=False)


