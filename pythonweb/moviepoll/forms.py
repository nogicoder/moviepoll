from .models import Question, Choice
from django.forms import (ModelForm, DateField, CharField,
                          Textarea, IntegerField)
from django.contrib.admin import widgets
from datetime import date, timedelta, datetime
from calendar import FRIDAY


class QuestionForm(ModelForm):

    pub_date = DateField(initial=datetime.now(), required=True)
    question_text = CharField(initial='Which movie to see this Friday',
                              widget=Textarea())

    class Meta:
        model = Question
        fields = [
            'question_text',
            'pub_date'
        ]


class ChoiceForm(ModelForm):
    votes = IntegerField(initial=0)

    class Meta:
        model = Choice
        # Not include question as a field
        exclude = ['question']
