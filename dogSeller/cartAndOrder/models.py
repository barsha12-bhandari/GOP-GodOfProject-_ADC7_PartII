from django.db import models
from viewDogs.models import *
from django.contrib.auth.models import User

class Order(models.Model):
    product = models.ManyToManyField(Dogs,blank=True)
    customer = models.ManyToManyField(User,blank=True)
    quantity = models.IntegerField()
    deliveryLocation = models.CharField(max_length=200)
    def __str__(self):
        return self.id

class Cart(models.Model):
    product = models.ManyToManyField(Dogs,blank=True)
    customer = models.ManyToManyField(User,blank=True)
    quantity = models.IntegerField()
    def __str__(self):
        return self.id    

