from django.db import models
from django.urls import reverse


# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=100)

    def get_url(self):
        return reverse('bankapp:index')

    def __str__(self):
        return self.name


class Branchs(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
