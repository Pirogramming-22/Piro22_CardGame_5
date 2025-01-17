#urls.py
from django.urls import path
from game import views
from . import views
from .views import dashboard_view
app_name = 'game'

urlpatterns = [
    # 영호
    path('game/history/' , views.gameHistory , name="gameHistory"),
    path('game/delete/<int:pk>/', views.delete_game, name='delete_game'),
    path('game/rankingTop3/' , views.gameRankingTop3 , name="gameRankingTop3"),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', views.base, name='base'),

    # 혜린
    path('game/start/', views.game_start_view, name='game_start_view'),
    path('game/attack/<int:pk>/', views.attack, name='attack'),
]