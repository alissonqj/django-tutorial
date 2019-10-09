from django.shortcuts import render, get_object_or_404  # Importar aqui
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_questions_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    response = f'Voce esta olhando para os resultados da questao {question_id}'
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f'Voce esta votando na questao {question_id}')
