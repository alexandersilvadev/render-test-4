from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
