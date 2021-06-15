from django.urls import path
from App_Login import  views

app_name = 'App_Login'

urlpatterns = [
    path('sign_up/',views.sign_up,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change-profile/',views.user_change,name='change-profile'),
    path('password/',views.pass_change,name='pass-change'),
    path('add-pro-pic/',views.add_pro_pic,name='add_pro_pic'),
    path('change-picture/',views.change_pro_pic,name='change_pro_pic'),
]
