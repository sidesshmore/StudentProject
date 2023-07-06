from django.db import models



# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=5)
    stream = models.CharField(max_length=10)
    fees_paid = models.BooleanField(default=True)

