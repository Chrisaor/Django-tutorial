from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.template import loader

from polls.models import Question, Choice


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

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question' : question,
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    '''
    1. request.POST의 choice키에 온 value를 HttpResonse로 출력
    choice객체의 votes값을 1 증가시키고 DB에 저장
    2. 이후 question_id에 해당하는 results뷰로 redirect
    '''
    choice_pk = request.POST['choice']
    choice = Choice.objects.get(pk=choice_pk)
    choice.votes += 1
    choice.save()

    return redirect(
        'polls:results',
        question_id=question_id
    )

def results(request, question_id):
    '''
    question_id에 해당하는 Question객체 한개를 넘김
    polls/results.html에서
    question에 속한 Choice들의 목록을 보여주면서
    각 항목의 votes값을 출력

    :param request:
    :param question_id:
    :return:
    '''
    question = Question.objects.get(pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', {'question':question})