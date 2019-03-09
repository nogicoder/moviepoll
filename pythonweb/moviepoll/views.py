from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import QuestionForm, ChoiceForm
from .models import Question, Choice
from django.http import HttpResponseRedirect


def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    return render(request, 'moviepoll/index.html')


def view_questions(request):
    questions = Question.objects.all().order_by('id')
    view_question_context = {
        'questions': questions
    }
    return render(request, 'moviepoll/questions.html', view_question_context)


def view_single_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choices.all().order_by('id')
    single_context = {
        'question': question,
        'choices': choices
    }
    return render(request, 'moviepoll/question_info.html', single_context)


def add_question(request, error=False):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        question = Question.objects.latest('id')
        return HttpResponseRedirect(reverse('add-choice', args=(question.id,)))
    else:
        if request.method == 'POST':
            error = True
    form = QuestionForm()
    question_context = {
        'form': form,
        'error': error
    }
    return render(request, 'moviepoll/add_question.html', question_context)


def add_choice(request, question_id, error=False):
    question = get_object_or_404(Question, pk=question_id)
    form = ChoiceForm(request.POST or None)
    if form.is_valid():
        choice = form.save(commit=False)
        choice.question = question
        choice.save()
        return HttpResponseRedirect('./')
    else:
        if request.method == 'POST':
            error = True
    form = ChoiceForm()
    choice_context = {
        'question': question,
        'form': form,
        'error': error
    }
    return render(request, 'moviepoll/add_choice.html', choice_context)


def add_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question=question_id).order_by('id')
    if request.method == 'POST':
        choice = request.POST.get('choice')
        vote = Choice.objects.get(pk=choice)
        vote.votes += 1
        vote.save()
        return HttpResponseRedirect('../')
    else:
        vote_context = {
            'question': question,
            'choices': choices
        }
        return render(request, 'moviepoll/add_vote.html', vote_context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choices.all().order_by('id')
    total = sum(choice.votes for choice in choices)
    for choice in choices:
        if total:
            choice.percent = int(choice.votes/total*100)
            choice.save()
    try:
        result = max(choices, key=lambda i: i.votes)
    except ValueError:
        result = ''
    results_context = {
        'question': question,
        'choices': choices,
        'result': result
    }
    return render(request, 'moviepoll/results.html', results_context)
