from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_Name = models.CharField(max_length=200)
    project_Location = models.CharField(max_length=100)
    project_Info = models.TextField(max_length=1000)
    project_Goal = models.BigIntegerField()
    project_Reach = models.BigIntegerField()
    project_Date = models.DateField()
    def __str__(self):
        return self.project_Name

class Donation(models.Model):
    donation_Id = models.AutoField(primary_key=True)
    user_Id = models.IntegerField()
    project_Id = models.IntegerField()
    donated = models.IntegerField()
    def __str__(self):
        user = User.objects.get(pk=self.user_Id)
        return user.username
