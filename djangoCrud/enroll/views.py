from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid() :
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else :
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu': stud})

def edit_show(request, id):
    stud = User.objects.get(pk=id)
    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=stud)
        if fm.is_valid() :
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(id, name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/')
    else :
        fm = StudentRegistration(instance=stud)
    return render(request, 'enroll/updatestudent.html', {'form':fm})

def delete_show(request, id):
    if request.method == 'POST':
        stud = User.objects.get(pk=id)
        stud.delete()
    return HttpResponseRedirect('/')