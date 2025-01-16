#urls.py
from django.urls import path
from game import views
from .views import dashboard_view, game_start_view, game_history_view
app_name = 'game'

urlpatterns = [
    path('game/history/' , views.gameHistory , name="gameHistory"),
    path('game/delete/<int:pk>/', views.delete_game, name='delete_game'),
    path('game/rankingTop3/' , views.gameRankingTop3 , name="gameRankingTop3"),
    path('game/ranking/' , views.gameRanking , name="gameRanking"),
    path('dashboard/', dashboard_view, name='dashboard'),
]