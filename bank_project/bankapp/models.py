from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class applicationform(models.Model):
    name=models.CharField(max_length=255)
    Date_of_Birth=models.CharField(max_length=255)
    age=models.IntegerField()
    gender=models.CharField(max_length=255)
    mail_id=models.CharField(max_length=255)
    phone=models.IntegerField()
    address=models.TextField()
    district=models.CharField(max_length=255)
    branch=models.CharField(max_length=255)
    account_ype=models.CharField(max_length=255)
    materials_to_provide=models.CharField(max_length=255)


