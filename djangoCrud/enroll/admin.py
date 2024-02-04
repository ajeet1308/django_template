from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin): 
    # Here we write those we want to see in our admin sqlit3
    list_display = ('id', 'name', 'email', 'password')
