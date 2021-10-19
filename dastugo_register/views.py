from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
from django.contrib import messages

# Create your views here.
def home(request):
   # return HttpResponse("<h1>Welcome to Cogut-Student Application</h1>")
   return render(request, "dastugo_register/home.html")

def student_list_view(request):
    students = Student.objects.all()
    
    context = {
        "students":students
    }
    return render(request, "dastugo_register/student_list.html", context)
    


def student_add_view(request):
    
    form = StudentForm()
    
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successful")
            return redirect("list_route")
            
    context ={
        "form" : form
    }
    return render(request, "dastugo_register/student_add.html", context)


def student_detail_view(request, pk):
    student = Student.objects.get(id = pk)
    
    context = {
        "student" : student
    }
    return render(request, "dastugo_register/student_detail.html", context)
    


def student_update_view(request, pk):
    student = Student.objects.get(id = pk)
    
    form = StudentForm(instance = student)
    
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance = student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully")
            return redirect("list_route")
    
    context = {
        "student" : student,
        "form" : form
    }
    
    return render(request, "dastugo_register/student_update.html", context)


def student_delete_view(request, pk):
    obj = Student.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('list_route')
    context = {
        "student": obj
    }
    return render(request, "dastugo_register/student_delete.html", context)