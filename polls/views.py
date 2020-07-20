from django.shortcuts import render
from django.http import request, HttpResponse, Http404, HttpResponseRedirect
from .models import Question
from django.urls import reverse

def index(request):
    q_list = Question.objects.order_by('pub_date')[:5]
    str_list = [q.question_text for q in q_list]
    html = ','.join(str_list)
    # return HttpResponse(html)
    return render(
        request, 'polls/index.html',
        { 'latest_question_list' : q_list})

def login(request):
    return render(request, 'polls/login.html')

def login_post(request):
    user_id = request.GET.get('아이뒹')
    user_pw = request.GET.get('비번비번')
    print(user_id,user_pw)
    request.session['user_id'] = user_id

    return HttpResponse('로귄완료')

def logout(request):
    request.session['user_id'] = None
    request.session.clear()
    return HttpResponse('잘가라 속세에서 벗어나라')

def index2(request):
    return render(request, 'polls/index2.html')

def reset(request, question_id):
    question = Question.objects.get(id=question_id)
    choice_list = question.choice_set.all()
    for choice in choice_list:
        choice.votes = 0
        choice.save()

    return HttpResponse('Ok')

def detail(request, question_id): # 질문 상세 페이지
    question = Question.objects.get(id=question_id)
    return render(
        request,'polls/detail.html',
        {'question' : question})

def results(request, question_id): # 투표 결과 페이지
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id): # 투표 페이지
    choice_id = request.POST['choice']
    #request.POST.get('choice')
    #질문 조회
    question = Question.objects.get(id=question_id)
    #보기 조회
    choice = question.choice_set.get(id = choice_id)
    #투표수 증가
    choice.votes += 1
    #저장
    choice.save()

    #return  HttpResponseRedirect('/polls/%s/' %question_id)
    return HttpResponseRedirect(reverse('detail', args=(question.id,)))
    #return HttpResponse("You're voting on question %s." % question_id)     