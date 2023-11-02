from django.db import models
import os


class Text(models.Model):
    file = models.FileField(upload_to='files', null=True)


def _delete_file(path):
    # Deletes file from filesystem.
    if os.path.isfile(path):
        os.remove(path)