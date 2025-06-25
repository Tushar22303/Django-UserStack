from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_page_view, name='profile_page_view'),
    path('profile/update/', views.update_profile_view, name='update_profile_view'),
]
