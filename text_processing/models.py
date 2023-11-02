from django.db import models


class Text(models.Model):
    file = models.FileField(upload_to='files', null=True)


