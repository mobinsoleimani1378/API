from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views

urlpatterns = [
    # path('user', views.UserData.as_view()),
    path('add', views.UserAdd.as_view()),
    path('login', views.signin.as_view()),
    path('logout', views.signout_user.as_view()),
    path('phone', views.OtpPhone.as_view()),
    path('code', views.OtpCode.as_view()),
    path('update/<int:id>', views.UpdateUser.as_view()),
]
