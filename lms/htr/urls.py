from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('learn/', views.learn, name='learn'),
    path('compete/', views.compete, name='compete'),
    path('practice/', views.practice, name='practice'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('rabk/', views.rank, name='rank'),
    path('ISO_27001/', views.ISO_27001, name='ISO_27001'),
    path('explore/', views.explore, name='explore'),

]
