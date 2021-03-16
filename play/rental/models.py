from django.db import models

from play.base.models import BaseModel


class Friend(BaseModel):
    name  = models.CharField(max_length=30)


class Belonging(BaseModel):
    name  = models.CharField(max_length=30)


class Borrowed(BaseModel):
    """Class that hold mail logic of Borrow relation"""

    what = models.ForeignKey(
        Belonging, 
        on_delete=models.CASCADE
    )

    to_who = models.ForeignKey(
        Friend, 
        on_delete=models.CASCADE
    )
    
    when = models.DateTimeField(
        auto_now_add=True
    )

    returned  = models.DateTimeField(
        null=True,
        blank=True
    )

        