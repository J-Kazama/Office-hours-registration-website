from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Schedule Your Office Hour Visit')
    #return render(request, 'professors/index.html')
