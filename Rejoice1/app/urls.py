from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path("<int:question_id>/question/", views.question, name = 'question'),
    path("<int:question_id>/result/", views.result, name = 'result'),
    path("<int:question_id>/vote/", views.vote, name = 'vote'),
    
]
