from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.method=='POST':
        uname= request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        cpass1=request.POST['cpassword']

        if pass1!=cpass1:
            return HttpResponse("password doesnot match")

        else:
            myuser= User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect('login')

    return render(request,'signup.html')





def loginpage(request):
    if request.method=='POST':
        uname= request.POST['name']
        pass1=request.POST['password']
        user=authenticate(request,username=uname,password=pass1)
        
     

        if user is not None:
           login(request,user)
           return redirect('home')

        else:
            return HttpResponse("username or password is incorrect")

    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
    