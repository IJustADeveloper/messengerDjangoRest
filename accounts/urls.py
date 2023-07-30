from django.urls import path
from .views import SignUp, personal_cabinet, logout_view

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('pers_cabinet', personal_cabinet, name="pers_cab"),
    path('log-out', logout_view, name='logout')
]