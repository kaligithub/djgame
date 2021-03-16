from django.db import models
from play.base.models import BaseModel



class Hero(BaseModel):
    name = models.CharField(max_length=30)
    alias = models.CharField(max_length=30)


    def __str__(self):
        return self.name
