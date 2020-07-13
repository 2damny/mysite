#view에 네개의 기능(색인, 세부, 결과, 투표 기능)만들기 

#from django.shortcuts import renders
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# 클래스 뷰 생성
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# Create your views here.
#클라이언트로부터 request를 받게되면 다시 response 해준다

#def index는 template를 로드해서 리스펀스
#context를 통해서 템플릿에 데이터를 전달

# def index(request):
    # 1
    # return HttpResponse("Hello, world")

    # 2
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    # 3 Use the temlplate
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))


    # 4 Use the shortcut - render
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list' : latest_question_list}
    # return render(request, 'polls/index.html',context)

# def detail(request, question_id):
    # 1 Basic View
    # return HttpResponse("You're looking at question %s." % question_id)
    
    # 2 Rasing a 404 error
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question':question})

    # 3 Use the shortcut - het_objext_or_404
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question':question})


# def results(request, question_id):
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        # question에서 외래키를 갖는 선택지를 가지고 오는 것.
        # 이때 조건은 선택지중에서 pk값이 템플릿에서 넘겨 받은 값을 조회하게 됨
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #데이터가 없는 경우except, 상세페이지를 보여줌
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message': "You didn't select a choice."})
    
    # 데이터가 있는 경우 선택지에 대해 표를 올려주고 저장, result url로 리다이렉트
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))