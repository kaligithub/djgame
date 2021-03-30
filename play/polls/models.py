import datetime
from django.db import models
from play.base.models import BaseModel

from django.utils import timezone


class Question(BaseModel):
    
    question_text = models.CharField(
        max_length=200
    )

    pub_date = models.DateTimeField('Published Date')


    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now    


class Choice(BaseModel):

    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE
    )

    choise_text  = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    votes = models.IntegerField(
       default=0
    )

    
    def __str__(self):
        return self.choise_text