from django.urls import path, re_path
from .views import (index, view_questions, view_single_question,
                    add_question, add_choice, add_vote, results)


urlpatterns = [
    path('', index),
    path('questions/', view_questions),
    path('questions/<int:question_id>/',
         view_single_question, name='view-single'),
    path('add_question/', add_question),
    path('questions/<int:question_id>/add_choice',
         add_choice, name='add-choice'),
    path('questions/<question_id>/vote/',
         add_vote, name='add-vote'),
    path('questions/<question_id>/results/',
         results, name='results'),
]
