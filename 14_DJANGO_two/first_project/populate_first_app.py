import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,Topic,Webpage,User
from faker import Faker

fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get a topic
        top=add_topic()

        #create fake data for entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        #create new webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

def populate_user(N=5):
    for entry in range(N):
        # get a topic
        name=fakegen.name().split()
        #create fake data for entry
        fake_first_name=name[0]
        fake_last_name=name[1]
        fake_email=fakegen.safe_email()

        #create new webpage entry
        user=User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]


if __name__=='__main__':
    print('populating script')
    populate(20)
    populate_user(20)
    print('populating complete')
