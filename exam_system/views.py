from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse

from .models import Questions
from .forms import QuestionsForm


@login_required(login_url='login')
def all_questions(request):
    questions = Questions.objects.all()

    template = 'exam_system/all_questions.html'
    context = {'questions': questions,}

    return render(request, template, context)


@login_required(login_url='login')
def question_details(request, id=id):
    single_question_details = Questions.objects.get(id=id)

    template = 'exam_system/question_details.html'
    context = {'single_question_details': single_question_details}

    return render(request, template, context)


@login_required(login_url='login')
def answer_details(request, id=id):
    pass




