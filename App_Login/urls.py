from django.urls import path
from . import views


app_name = 'App_Login'

urlpatterns = [
    path('signup/',views.Sign_up,name='signup'),
    path('login/',views.Login_Page,name='login'),
    path('logout/',views.Log_out,name='logout'),
    path('profile/',views.Profile_Page,name='profile'),
    path('edit/',views.Edit_Info,name='edit'),
    path('add_pro_pic/',views.Add_Profile_Pic,name='add_pro_pic'),
    path('change_profile_pic/',views.change_profile_pic,name='change-profile-pic'),
    path('password/',views.pass_change,name='password')
]
