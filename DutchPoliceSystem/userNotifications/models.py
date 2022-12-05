from django.db import models

# Create your models here.
class UploadDataModel(models.Model):

    title = models.CharField(max_length = 80, default="")
    file = models.FileField(upload_to='file/', default="")
    first_name = models.CharField(max_length = 50, default="")
    last_name = models.CharField(max_length = 50, default="")
    email = models.EmailField(max_length = 80, default="")
    description = models.TextField(max_length = 1000, default="")

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.last_name}"

class CreateNewMessage(models.Model):
    priorityLevel = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    status=(
        ('open','Open'),
        ('closed','Resolved')
    )
    date = models.DateField()
    name= models.CharField(max_length= 45)
    email = models.CharField(max_length=50)
    content= models.TextField(max_length=100)
    levelOfPriority = models.CharField(max_length=6, choices=priorityLevel)
    status = models.CharField(max_length=6, choices=status ,default="open")

