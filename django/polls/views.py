from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.template import loader

from polls.models import Question


def index(request):
    # 가장 최근에 발행된 5개의 Question목록
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 쉼표단위로 구분된 Question목록의 각 항목의 Question_text로 만들어진 문자열
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    # 장고 공식문서는 다음과 같다.
    # template = loader.get_template('polls/index.html')
    # context = {
    #    'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
def detail(request, question_id):

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

