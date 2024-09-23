from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('signup', views.signup,name="signup"),
    path('login', views.login,name="login"),
    path('privacy', views.privacy,name="privacy"),
    path('team', views.team,name="team"),
    path('chat', views.chat,name="chat"),
    path('bot', views.bot,name="bot"),
    
    path('signout', views.signout, name='signout'),
   
]