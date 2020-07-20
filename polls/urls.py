
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index2/', views.index2),
    path('login/', views.login),
    path('login_post/', views.login_post),
    path('logout/', views.logout),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('<int:question_id>/results/', views.results),
    path('<int:question_id>/votes/', views.vote, name = 'vote'),
    path('<int:question_id>/reset/', views.reset, name = 'reset'),
]
