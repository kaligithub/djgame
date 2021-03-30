from django.db import models
from play.base.models import BaseModel



class Hero(BaseModel):
    name = models.CharField(max_length=30)
    alias = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class Place(BaseModel):
    
    name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
    )

    address = models.CharField(
        max_length=80
    )

    def __str__(self):
        return self.name


class Restaurant(BaseModel):

    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
    )

    serve_hot_dogs = models.BooleanField(
        default=False
    )

    serve_pizza = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.place.name


class Waiter(BaseModel):
    
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name