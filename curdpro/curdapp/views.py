from django.shortcuts import render,redirect
from .models import StudentsData

def homepage(request):
    students=StudentsData.objects.all()
    return render(request, 'homepage.html',{'students':students})
def add_student(request):
    if request.method =='GET':
        return render(request,'add_student.html')
    else:
        StudentsData(
        first_name=request.POST.get('fname'),
        last_name=request.POST.get('lname'),
        course=request.POST.get('course'),
        fee=request.POST.get('fee'),
        assignment1=request.POST.get('assignment1'),
        assignment2=request.POST.get('assignment2'),
        assignment3=request.POST.get('assignment3'),
        assignment4=request.POST.get('assignment4'),
        institute=request.POST.get('institute'),
        location=request.POST.get('location')
        ).save()
        return redirect('homepage')
def update_student(request,id):
    student=StudentsData.objects.get(id=id)
    if request.method =='GET':
        return render(request, 'update_student.html',{'student':student})
    else:
        student.first_name=request.POST.get('fname')
        student.last_name=request.POST.get('lname')
        student.course=request.POST.get('course')
        student.fee=request.POST.get('fee')
        student.assignment1=request.POST.get('assignment1')
        student.assignment2=request.POST.get('assignment2')
        student.assignment3=request.POST.get('assignment3')
        student.assignment4=request.POST.get('assignment4')
        student.institute=request.POST.get('institute')
        student.location=request.POST.get('location')
        student.save()
        return redirect('homepage')
def Delete_Student(request,id):
    Student=StudentsData.objects.get(id=id)
    Student.delete()
    return redirect('homepage')
