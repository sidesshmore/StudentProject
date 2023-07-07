from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','roll_no','stream','fees_paid')
    list_editable=('fees_paid',)
    search_fields=('name','roll_no')
    list_filter=('stream','fees_paid')





admin.site.register(StudentModel, StudentAdmin)
# 