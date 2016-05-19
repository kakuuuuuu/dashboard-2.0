from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import forms, login, authenticate, logout
from forms import RegisterForm
from models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
class Register(View):
    form = RegisterForm
    def get(self, request):
        if request.user.is_authenticated() and request.user.is_staff==False:
            return redirect('/dashboard')
        context={'form':self.form()}
        return render(request, 'accounts/register.html', context)
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            print 'success'
            return redirect('/dashboard/')
        else:
            context={'form':form}
            print 'failure'
            return render(request,'accounts/register.html', context)
class Login(View):
    form = forms.AuthenticationForm
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/dashboard')
        context = {'form': self.form()}
        return render(request, 'accounts/login.html',context)
    def post(self, request):
        form=self.form(None,request.POST)
        context = {'form': form}
        if form.is_valid():
            print 'formisvalid'
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                print 'success'
                login(request, user)
                return redirect('/dashboard/')
            else:
                print 'failure'
                return render(request, 'accounts/login.html', context)
        else:
            return render(request, 'accounts/login.html', context)
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/accounts/login')
def delete(request,user_id):
    user=User.objects.get(id=user_id)
    if user.is_superuser:
        messages.error(request, 'You do not have the permission to delete that admin')
        return redirect('/dashboard')

    UserProfile.objects.get(user=user).delete()
    user.delete()
    return redirect('/dashboard')
def edit(request,user_id):
    user = User.objects.get(id=user_id)
    if user!=request.user and request.user.is_staff==False:
        messages.error(request, "You do not have the permissions to edit other user's information")
        return redirect('/dashboard')
    currentuser = request.user
    profile = UserProfile.objects.get(user=user)
    context={
        'user':user,
        'currentuser':currentuser,
        'profile':profile
    }
    return render(request,'accounts/edit.html', context)
def update(request,user_id):
    user = User.objects.get(id=user_id)
    if user.is_superuser==True and user!=request.user:
        messages.error(request, 'You do not have the permission to edit this user')

    else:
        User.objects.filter(id=user_id).update(email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'])
        if 'description' in request.POST:
            UserProfile.objects.filter(user=user).update(description=request.POST['description'])
            return redirect('/dashboard')
        else:
            if 'level' in request.POST:
                if request.POST['level']=='admin':
                    user.is_staff = True
                else:
                    user.is_staff = False
            user.save()
    return redirect('/dashboard')
def updatepass(request,user_id):
    user = User.objects.get(id=user_id)
    if user.is_superuser==True and user!=request.user:
        messages.error(request, 'You do not have the permission to edit this user')
    else:
        if request.POST['password1']==request.POST['password2']:
            user.set_password(request.POST['password1'])
            user.save()
        else:
            message.error(request, 'Password must match confirmation')
    return redirect('/dashboard')
# Create your views here.
