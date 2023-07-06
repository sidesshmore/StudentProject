from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def portal(request):
    students = StudentModel.objects.all()
    return render(request, 'studentapp/portal.html', { 'students' : students})



def add_student(request):
    if request.method == 'POST':
        # data fetch
        student_name = request.POST.get('name')
        student_roll = request.POST.get('roll_no')
        student_stream = request.POST.get('stream')
        student_fees = request.POST.get('fees')


        # create model object and set data
        student = StudentModel()
        student.name = student_name
        student.roll_no = student_roll
        student.stream = student_stream
        student.fees_paid = student_fees
        if student_fees in ['None', '']:
            student.fees_paid = False
        else:
            student.fees_paid = bool(student_fees)


        # save object
        student.save()
        return redirect('/student/portal/')


    return render(request, 'studentapp/add_student.html')


def update_student(request, roll_no):
    student = StudentModel.objects.get(pk=roll_no)
    return render(request, 'studentapp/update_student.html', {'student' : student})


def make_update(request, roll_no):
    # data fetch
        student_name = request.POST.get('name')
        student_roll_temp = request.POST.get('roll_no')
        student_stream = request.POST.get('stream')
        student_fees = request.POST.get('fees')

        # create model object and set data
        student = StudentModel.objects.get(pk=roll_no)

        student.name = student_name
        student.roll_no = student_roll_temp
        student.stream = student_stream
        student.fees_paid = student_fees
        if student_fees in ['None', '']:
            student.fees_paid = False
        else:
            student.fees_paid = bool(student_fees)
        
        student.save()
        return redirect('/student/portal/')


def delete_student(request, roll_no):
    student = StudentModel.objects.get(pk=roll_no)
    student.delete()

    
    return redirect('/student/portal/')
