from django.db import models


# I Create models here for creating table int database.
class personal_details(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact=models.BigIntegerField()
    adress=models.CharField(max_length=50)



