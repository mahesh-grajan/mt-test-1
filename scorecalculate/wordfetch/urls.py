from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='getword'),
    path('listscores/', views.list_scores, name='listscores'),
    path('displayscores/', views.display_scores, name='displayscores')
]
