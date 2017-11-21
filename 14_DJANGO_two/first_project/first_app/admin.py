from django.contrib import admin
from first_app.models import Topic,AccessRecord,Webpage,User

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)
