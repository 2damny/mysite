import datetime

from django.db import models
from django.utils import timezone

#Question모델은 질문과 발행일을 위한 필드를 구성

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

#어제의 시간 반환, 어제 이후에 발행이 된 데이터 리턴
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


#Choice모델은 선택지(choice)와 표계산(vote)을 위한 필드를 구성
#Choice모델은 Question모델과 연관(외래키)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text