from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('portal/', portal),
    path('add/', add_student),
    path('update/<str:roll_no>/', update_student),
    path('make-update/<str:roll_no>/', make_update),
    path('delete/<str:roll_no>/', delete_student),

]