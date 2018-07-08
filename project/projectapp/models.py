from django.db import models

class FileUpload(models.Model):
  file_name = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20,blank=True,null=True)
  timestamp = models.DateTimeField(auto_now_add=True)
      

