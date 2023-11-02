from django.db import models


class Pesel(models.Model):
    pesel = models.CharField(max_length=11)
