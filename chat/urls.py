from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.signup),
    path("register", views.register),
    path("chatbot",views.chatbot),
    path("profile",views.profile),
    path("logout",views.logout),
]
