from django.urls import path

from accaunts.views import register_part, login_part, logout_part

urlpatterns = [
    path('register/', register_part, name='register'),
    path('login/', login_part, name='login'),
    path('logout/', logout_part, name='logout')

]