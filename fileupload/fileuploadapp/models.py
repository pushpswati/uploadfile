from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UploadMedia(models.Model):
    file_name = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['uploaded_at']
