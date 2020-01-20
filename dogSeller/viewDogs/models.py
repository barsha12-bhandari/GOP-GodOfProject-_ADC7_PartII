from django.db import models

# Create your models here.
class Dogs(models.Model):
    name = models.CharField(max_length= 255)
    price = models.IntegerField()
    stockNo = models.IntegerField()
    image = models.ImageField(upload_to='media/images/')
    breed = models.CharField(max_length=255)
    weight = models.IntegerField()
    description = models.CharField(max_length= 255)

    def __str__(self):
        return (self.name)
    #abstract model which allows inheritance and the table is not created
    class Meta:
        abstract = True
        # ordering = ["name","price","stockNo","releaseDate","specs","brand","image"]

