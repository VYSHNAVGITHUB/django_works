from django.db import models

class Cakes(models.Model):
    name=models.CharField(max_length=250,unique=True)
    flavour=models.CharField(max_length=250)
    price=models.PositiveIntegerField()
    shape=models.CharField(max_length=200)
    weight=models.CharField(max_length=150)
    layer=models.CharField(max_length=200)
    description=models.CharField(max_length=500)


    def __str__(self) -> str:
        return self.name
