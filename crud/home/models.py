from django.db import models

# Create your models here.
class family(models.Model):
    Id=models.CharField(max_length=10,primary_key=True)
    Name=models.CharField(max_length=200)
    Surname=models.CharField(max_length=200)
    Age=models.IntegerField()
    