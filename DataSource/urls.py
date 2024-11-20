from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home.as_view(),name='index'),
    path('signup',views.signup,name='signup_form'),
    path('signup_request',views.createNewMember,name='create_new_user'),
    # path('login/',views.login,name='login_form'),
    path('send-message',views.sendMessage,name="send_message"),
    path('api/',views.sendMessage,name="send_message"),
    path('api/store',views.sendMessage,name="send_message"),

    path('vr-list/', views.VRModelListView.as_view(), name='vr_model_list'),


    ## Auth Path
    path('login/', views.LoginView.as_view(), name="login_form"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]