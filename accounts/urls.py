from django.urls import path, include
from . import views

app_name = 'accounts'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/<slug:slug>', views.profile, name='profile'),

] 