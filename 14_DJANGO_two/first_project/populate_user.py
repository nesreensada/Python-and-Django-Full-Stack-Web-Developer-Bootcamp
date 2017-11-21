import random
from first_app.models import User
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        # get a topic

        #create fake data for entry
        fake_first_name=fakegen.name()
        fake_last_name=fakegen.name()
        fake_email=fakegen.safe_email()

        #create new webpage entry
        user=User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]



if __name__=='__main__':
    print('populating script')
    populate(20)
    print('populating complete')
