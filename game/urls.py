#urls.py
from django.urls import path
from game import views
from . import views
from .views import dashboard_view
app_name = 'game'

urlpatterns = [
    # 영호
    path('game/history/' , views.gameHistory , name="gameHistory"), #1
    path('game/delete/<int:pk>/', views.delete_game, name='delete_game'), #2
    path('game/rankingTop3/' , views.gameRankingTop3 , name="gameRankingTop3"), #3
    path('dashboard/', dashboard_view, name='dashboard'), #4
    path('', views.base, name='base'),#5
    # 혜린
    path('game/detail/<int:pk>/', views.game_detail, name='game_detail'), #8
    path('game/start/', views.game_start_view, name='game_start_view'),
    path('game/create/', views.create_game, name='create_game'),
    path('game/counterattack/<int:pk>/', views.go_counterattack, name="counterattack"),
    path('game/before_detail/<int:pk>/', views.before_detail, name="before_detail"),
]