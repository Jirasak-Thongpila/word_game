from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/get-word/', views.get_random_word, name='get_random_word'),
    path('api/check-word/', views.check_word, name='check_word'),
    path('api/save-score/', views.save_score, name='save_score'),
]
