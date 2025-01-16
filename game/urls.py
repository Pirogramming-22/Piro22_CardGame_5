#urls.py
from django.urls import path
from game import views

app_name = 'game'

urlpatterns = [
    path('game/history/' , views.gameHistory , name="gameHistory"),
    path('game/rankingTop3/' , views.gameRankingTop3 , name="gameRankingTop3"),
    path('game/ranking/' , views.gameRanking , name="gameRanking"),
]