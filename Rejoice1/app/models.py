import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=70)
    pub_date = models.DateTimeField("Date Published")
    Date_of_birth = models.CharField(max_length=20)
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    # def birth_day(self):
    #     return self.Date_of_birth < timezone.now - datetime.timedelta(days=2)
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_questions = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
