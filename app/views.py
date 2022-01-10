
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
from django.views.generic import CreateView, FormView, UpdateView , ListView
from django.urls import reverse_lazy
from app.models import StudentInfo,StudentAcademics
 
# Relative import of GeeksForm
from .forms import LoginRegisterForm,ProfileForm,AcademicForm
import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/'


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('addinfo')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, "Username does not exist")
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('addinfo')
        else:
            print("Incorrect")

    return render(request,"student/login_register.html")

def logoutPage(request):
    logout(request)
    messages.info(request,"You are logged out")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = LoginRegisterForm()

    if request.method == 'POST':
        form = LoginRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"User account has been created successfully!")
            login(request,user)
            return redirect('addinfo')
        else:
            messages.error(request,"An error occurred")
    context = {'page':page,'form':form}
    return render(request,'student/login_register.html',context)

@login_required(login_url='login')
def addStudentinfo(request):
    profile = request.user.studentinfo
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request,"student/addinfo.html",context)

@login_required(login_url='login')
def addStudentacademics(request):
    profile = request.user.studentinfo
    form = AcademicForm()

    if request.method == 'POST':
        form = AcademicForm(request.POST,request.FILES)
        if form.is_valid():
            academics = form.save(commit=False)
            academics.rollno = profile
            academics.save()
            return redirect('login')
    context = {'form':form}
    return render(request,"student/studentacademics.html",context)

def Studentdetails(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    student_details = StudentInfo.objects.filter(
        Q(username__icontains=search_query)
    )
    context = {
        'student_details':student_details
    }

    return render(request,'student/student_details.html',context)

def academicslist(request,pk):
    academiclist = StudentAcademics.objects.get(rollno=pk)
    activity = academiclist.studentacademic_set.all()
    context = {'academiclist':academiclist,'activity':activity}
    return render(request,'student/academiclist.html',context)



