from django.db import models

from play.base.models import BaseModel


class Employee(BaseModel):

    regNo = models.CharField(
        max_length=30,
    )

    name  = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        max_length=254
    )

    mobile = models.CharField(
        max_length=30
    )
    address = models.TextField(
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        blank=True,
        null=True,
    )
    