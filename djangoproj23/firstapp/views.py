from django.shortcuts import render
from firstapp.forms import UserAdditional_form, UserProfile_form

#for login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'firstapp/index.html')

def register(request):
    registered=False
    UserProfile_View=UserProfile_form()
    UserAdditional_View=UserAdditional_form()
    if request.method =='POST':
        UserProfile_View=UserProfile_form(request.POST)
        UserAdditional_View=UserAdditional_form(request.POST)
        if UserProfile_View.is_valid() and UserAdditional_View.is_valid():
            buser=UserProfile_View.save()
            pw=buser.password
            buser.set_password(pw)
            buser.save()

            additional=UserAdditional_View.save(commit=False)
            additional.user=buser
            if 'profile_pic' in request.FILES:
                additional.profile_pic=request.FILES['profile_pic']
            additional.save()
            registered=True
        else:
            print(UserProfile_View.errors,UserAdditional_View.errors)
    else:
        UserProfile_View=UserProfile_form()
        UserAdditional_View=UserAdditional_form()
    return render(request, 'firstapp/register.html',{'key1': UserProfile_View, 'key2': UserAdditional_View,'key3':registered})


def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            print('Someone tried to login and failed')
            print('Usename: {} and password: {}'.format(username, password))
            return HttpResponse('Invalid login details entered!')
    else:
        return render(request,'firstapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('You are logged in@ Ur Account!')
