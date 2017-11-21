from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello there')
def help(request):
    my_dict={'insert_here':'help page'}
    return render(request,'apptwo/help.html',context=my_dict)
