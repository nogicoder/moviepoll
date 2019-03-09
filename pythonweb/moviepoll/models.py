from django.db.models import (Model, CharField, DateField,
                              ForeignKey, IntegerField, CASCADE)
from django.forms import ModelForm


class Question(Model):
    question_text = CharField(
        max_length=200,
        unique=True
    )
    pub_date = DateField('Publish Date')

    def __str__(self):
        return self.question_text


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE, related_name='choices')
    choice_text = CharField(blank=False, default='',
                            max_length=200, unique=True)
    votes = IntegerField(default=0)
    percent = IntegerField(default=0)

    def __str__(self):
        return self.choice_text
