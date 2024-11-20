from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home.as_view(),name='index'),
    path('send-message',views.sendMessage,name="send_message"),
    path('api/',views.sendMessage,name="send_message"),

    path('vr-list/', views.VRModelListView.as_view(), name='vr_model_list'),


    ## Auth Path
    path('login/', views.LoginView.as_view(), name="login_form"),
    path('signup/', views.SignupView.as_view(), name="signup_form"),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    ## API's URL
    path('api/countries/', views.CountryListAPIView.as_view(), name='country-list'),
]