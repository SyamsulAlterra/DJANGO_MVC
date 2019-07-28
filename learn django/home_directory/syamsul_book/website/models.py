from django.db import models
from django.utils.timezone import now

# Create your models here.
class Orang(models.Model):
    name=models.CharField(max_length=200)
    # birth_date=models.DateField()
    address=models.TextField()
    email=models.EmailField()
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    join_date=models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class login_person(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        self.username