from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
# Create your views here.

def index(request):
    return HttpResponse('Index Page')

def results(request, question_number):
    return HttpResponse('You are looking at Questions: %s' %question_number)

def checkList(request, check_number):
    return HttpResponse('See at the Check List: %s' %check_number)

def allResults(request):
    output = Students.objects.all().order_by('std_name')
    # result = ','.join([str(q.std_age) for q in output])
    return render(request, 'temp.html', {'output':output})
