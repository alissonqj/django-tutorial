import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __repr__(self):
        return f"<ID {self.pk}> <Text: {self.question_text}>"

    def __str__(self):
        return f"<ID {self.pk}> <Text: {self.question_text}>"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"<ID {self.pk}> <Text: {self.choice_text}>"

    def __repr__(self):
        return f"<ID {self.pk}> <Text: {self.choice_text}>"
        # return "<ID: {}> <Text: {}>".format(self.pk, self.choice_text)
