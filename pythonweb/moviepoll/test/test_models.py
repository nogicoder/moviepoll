from django.test import TestCase
from moviepoll.models import Question, Choice


class QuestionTestCase(TestCase):
    def set_up(self):
        Question.objects.create(question_text='What to eat?', pub_date='12/09/2019')

    def test_question(self):
        place = Question.objects.all()
        print(place)