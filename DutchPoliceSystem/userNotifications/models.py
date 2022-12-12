from django.db import models

# Create your models here.




class CreateNewMessage(models.Model):
    # Define message priority value and status value

    priorityLevel = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )

    # Define message field varibale, type and setting
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
