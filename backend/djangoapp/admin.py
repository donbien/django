from django.contrib import admin
from djangoapp.models import User, Patient, Blood_group, Name

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Blood_group)
admin.site.register(Name)

# Register your models here.
