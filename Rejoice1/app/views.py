from django.shortcuts import render
from django.http import HttpResponse
from . models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app/index.html', context)

    
def about(request):
    return HttpResponse("<h1 style='color: red' >Hello, my name is Rejoice</h1>")

def question(request, question_id):
    return HttpResponse("You are looking at question %s" %question_id)

def result(request, question_id):
    return HttpResponse("This is result number %s" %question_id)

def vote(request, question_id):
    response = "<h1>You are voting on question %s</h1>"
    return HttpResponse(response % question_id)
    
