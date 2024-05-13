from django.urls import path
from .views import login_user,logout_user, signup_view


urlpatterns = [
    path('', login_user, name='login'),
    path('logout_user', logout_user, name='logout'),
    path('signup/', signup_view, name='signup'),
]
