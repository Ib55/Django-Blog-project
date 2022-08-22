
from django.shortcuts import render
from App_Login.forms import Signup,EditInfo,ProfilePic,PassChange
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def Sign_up(request):
    form = Signup()
    registered = False
    if request.method == 'POST':
        form = Signup(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request,'App_Login/sign_up.html',context={'form':form,'registered':registered})

def Login_Page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Blog:home'))
            
            
    return render(request,'App_Login/login.html',context={'form':form})

@login_required
def Log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Blog:home'))

@login_required
def Profile_Page(request):
    return render(request,'App_Login/profile.html',context={})

@login_required
def Edit_Info(request):
    current_user = request.user
    change = False
    form = EditInfo(instance=current_user)
    if request.method == 'POST':
        form = EditInfo(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form = EditInfo(instance=current_user)
            change = True
            pass
    return render(request,'App_Login/edit_info.html',context={'form':form,'change':change})

@login_required
def Add_Profile_Pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/add_pro_pic.html',context={'form':form})

@login_required
def change_profile_pic(request):
    
    form = ProfilePic(instance=request.user.profile_user)
    if request.method == 'POST':
        form = ProfilePic(request.POST,request.FILES,instance=request.user.profile_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/add_pro_pic.html',context={'form':form})



# @login_required
# def pass_change(request):
#     current_user = request.user
#     form = PasswordChangeForm(current_user)
#     change = False
#     if request.method == 'POST':
#         form = PasswordChangeForm(current_user,data=request.POST)
#         if form.is_valid():
#             form.save()
#             change = True
#     return render(request,'App_Login/pass_change.html',context={'form':form,'change':change})


@login_required 
def pass_change(request):
    current_user = request.user
    change = False
    form = PassChange(current_user)
    if request.method == 'POST':
        form = PassChange(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            change = True
    return render(request,'App_Login/pass_change.html',context={'form':form,'change':change})