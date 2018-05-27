from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


def upload_to(instance,file_name):
    now = timezone.now()
    extension = file_name.split(".")[-1]

    if extension in ["mp4", 'mkv','.avi','.3gp']:
        #import pdb;pdb.set_trace()
        folder = "videos"
    elif extension in ['jpg', 'jpeg', 'png']:
        folder = "pictures"
    else:
        folder = "content"

    return "uploads/{year}/{month}/{day}/{folder}/{file_name}".format(
        year=now.year, month=now.month, day=now.day, folder=folder, file_name=file_name)


class UploadFile(models.Model):
    file = models.FileField(upload_to=upload_to, blank=True, null=True)
    def __str__(self):
        return self.file

