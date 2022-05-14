from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register', views.register, name='reg'),
    path('login', views.LoginUserView.as_view(), name='login'),
    #path('change', views.UserChangePassword.as_view(), name='change'),
    path('profile', views.profile, name='prof'),
]
