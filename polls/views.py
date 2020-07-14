from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    q_list = Question.objects.order_by('pub_date')[:5]
    str_list = [q.question_text for q in q_list]
    html = ','.join(str_list)
    # return HttpResponse(html)
    return render(
        request, 'index.html',
        { 'latest_question_list' : q_list})

def detail(request, question_id): # 질문 상세 페이지
    question = Question.objects.get(id=question_id);
    return render(
        request,'polls/detail.html',
        {'question' : question})

def results(request, question_id): # 투표 결과 페이지
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id): # 투표 페이지
    return HttpResponse("You're voting on question %s." % question_id)