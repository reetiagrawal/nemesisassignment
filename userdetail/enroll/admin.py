from django.contrib import admin
from .models import FullDetail
from .models import User

# Register your models here.
admin.site.register(FullDetail)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email')
