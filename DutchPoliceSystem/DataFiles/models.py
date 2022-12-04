from django.db import models

# Create your models here.
class UploadDataModel(models.Model):

    title = models.CharField(max_length = 80, default="")
    file = models.FileField(upload_to='file/', default="")
    first_name = models.CharField(max_length = 50, default="")
    last_name = models.CharField(max_length = 50, default="")
    email = models.EmailField(max_length = 80, default="")
    desc = models.TextField(max_length = 1000, default="")

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.last_name}"
