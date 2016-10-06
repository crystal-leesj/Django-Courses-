from django.shortcuts import render, redirect
from datetime import datetime
from .models import Course

def index(request):
    context = {
        "courses" : Course.objects.all()
    }
    return render(request, 'coursesApp/index.html', context)

def add_course(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    context = {
        "course" : Course.objects.get(id=id)
    }
    return render(request, 'coursesApp/delete.html', context)

def remove_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')
