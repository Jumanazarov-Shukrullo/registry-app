from django.db import models


class Table(models.Model):
    fullname = models.TextField(null=True, blank=True)
    abbreviated_name = models.CharField(max_length=255, null=True, blank=True)
    licence_number = models.CharField(max_length=16, null=True, blank=True)
    inn = models.BigIntegerField(null=True, blank=True)
    date_of_registration = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=32, null=True, blank=True)
    termination_date = models.DateField(null=True, blank=True)