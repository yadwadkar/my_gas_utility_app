from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Customer, SupportRepresentative

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(SupportRepresentative)
