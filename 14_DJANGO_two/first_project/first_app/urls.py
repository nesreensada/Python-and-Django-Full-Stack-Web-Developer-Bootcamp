from django.conf.urls import url
from first_app import views

urlpatterns = [

    url(r'^$',views.users,name='users'),
]
