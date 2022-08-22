




from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from App_Login.models import Profile


style = 'margin-bottom:1rem'
class Signup(UserCreationForm):
    username = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username','style':style}))
    email = forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Email','style':style}))
    password1 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password','style':style}))
    password2 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Again Password','style':style}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class EditInfo(UserChangeForm):
    username = forms.CharField(label='',required=True,widget=forms.TextInput(attrs={'placeholder':'Username','style':style}))
    email = forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Email','style':style}))
    first_name = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'First Name','style':style}))
    last_name = forms.CharField(required=True,label = '',widget=forms.TextInput(attrs={'placeholder':'Last Name','style':style}))   
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')



class ProfilePic(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic',]


class PassChange(PasswordChangeForm):
    old_password = forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={'placeholder':'Old Password','style':style}))
    new_password1 = forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={'placeholder':'New Password','style':style}))
    new_password2 = forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={'placeholder':'New Password Again','style':style}))
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')