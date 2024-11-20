from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from django.urls import path
from . import views


urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #path('send-message/',views.sendMessage,name="send_message"),
    path('get-users/',views.getUsers.as_view()),
    path('get-vr-data',views.getVRModelData),
    path('store-vr-data',views.postVRModelData),

]