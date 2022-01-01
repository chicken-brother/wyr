from django.shortcuts import redirect, render
from .models import Question

def home(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'base/home.html', context)

def question(request, pk):
    question = Question.objects.get(id=pk)
    print(question)
    context = {'question': question}
    return render(request, 'base/question.html', context)
