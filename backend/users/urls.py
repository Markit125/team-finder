from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from . import views
from .forms import LoginForm

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile'),
    path('profile/edit/', views.ProfileUpdate.as_view(), name='profile_edit'),
    path('list/', views.UserList.as_view(), name='user_list'),
    path('password_change/', 
         PasswordChangeView.as_view(template_name='users/password_change.html', success_url='/'), 
         name='password_change'),
]