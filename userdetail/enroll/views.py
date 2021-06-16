from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import SignUpForm,InfoProfileForm,StudentRegistration
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

def sign_up(request):
    register = False
    if request.method == 'POST':
       signup_form = SignUpForm(data = request.POST)
       info_form = InfoProfileForm(data = request.POST)
       if signup_form.is_valid() and info_form.is_valid():
           user = signup_form.save()
           user.save()
           profile = info_form.save(commit=False)
           profile.user = user
           profile.save()
           register =True
       else:
           HttpResponse("<h1>Something went wrong</h1>")
    else:
        signup_form = SignUpForm(data = request.POST)
        info_form = InfoProfileForm(data= request.POST)
    return render(request,'registration.html', {
        'signup_form':signup_form,
        'info_form' : info_form,
        'register':register
    })

#Login Function

def user_login(request):
    if request.method == "POST":
         fm=AuthenticationForm(request=request , data=request.POST)
         if fm.is_valid():
             uname= fm.cleaned_data['username']
             upass = fm.cleaned_data['password']
             user=authenticate(username=uname,password=upass)
             if user is not None:
                 login(request,user)
                 return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request,'userlogin.html',{'form': fm})

#profile
def user_profile(request):
    return render(request,'profile.html')

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def add_show(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
    else:
        fm = SignUpForm()
    stud = User.objects.all()
    return render(request,'addandshow.html',{'form':fm , 'stu':stud})

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = SignUpForm(request.POST,instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = SignUpForm(instance=pi)
    return render(request,'update.html',{'form':fm})

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = [UserSerializer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]