from django.db import models



class Person(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255)
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    age = models.IntegerField(null =True, blank = True)
    class Meta:
        managed = True
        
class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.CharField(max_length=50)
    name2 = models.CharField(max_length=50)
    age = models.IntegerField()
    color = models.CharField(max_length=50)
    weight = models.IntegerField()
    owner = models.ForeignKey(
        'Person', 
        on_delete=models.CASCADE,
        null = True)
    class Meta:
        managed = True


# Create your models here.
