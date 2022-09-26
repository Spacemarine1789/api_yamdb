# from django.contrib import admin
# from .models import User

# admin.site.register(User) 


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomAdmin(UserAdmin):
    pass

# admin.site.register(User, CustomAdmin)
admin.site.register(User)