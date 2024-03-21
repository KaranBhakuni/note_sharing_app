from django.shortcuts import render

# Create your views here.
def home(request):
    context={'page':'home'}
    return render(request, "home.html",context)

def registration(request):
    return render(request,"registration.html")

def login(request):
    return render(request, "login.html")

def student_home(request):
    return render(request,"student_home.html")