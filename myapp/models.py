from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
   

class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=20)
   
