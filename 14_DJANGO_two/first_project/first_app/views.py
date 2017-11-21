from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage,User
# Create your views here.
def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    return render(request,'first_app/index.html',context=date_dict)

def users(request):
    users_list=User.objects.order_by('first_name')
    user_dict={'user_records':users_list}
    return render(request,'first_app/users.html',context=user_dict)
