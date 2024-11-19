from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup_form'),
    path('signup_request',views.createNewMember,name='create_new_user'),
    path('login',views.login,name='login_form'),
    path('send-message',views.sendMessage,name="send_message"),
    path('api/',views.sendMessage,name="send_message"),
]