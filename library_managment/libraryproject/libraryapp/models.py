from django.db import models


# Create your models here.


class Admin(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    emailid = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    Objects = models.Manager()

    class Meta:
        db_table = 'admin'


class Book(models.Model):
    bookname = models.CharField(max_length=50, primary_key=True)
    Authorname = models.CharField(max_length=50, blank=True, null=True)
    bookprice = models.CharField(max_length=50, blank=True, null=True)
    booklocation = models.CharField(max_length=50, blank=True, null=True)
    Objects = models.Manager()

    class Meta:
        db_table = 'book'
