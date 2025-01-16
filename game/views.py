from django.shortcuts import render,redirect
from .models import Game
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

def gameHistory(request):
    games = Game.objects.filter(Q(player1 = request.user)| Q(player2 = request.user))
    user = request.user
    ctx = {
        'games' : games,
        'user' : user ,
    }
    return render(request , 'game/Game-History.html' , context = ctx)

def gameRankingTop3(request):
    users=User.objects.all()
    top3_users = users.order_by('-win_count')[:3]
    ctx = {
        'top3_users' : top3_users ,
    }
    return render(request , 'game/Game-Ranking-Top3.html' , context = ctx)

def gameRanking(request):
    users=User.objects.all()
    ctx = {
        'users' : users ,
    }
    return render(request , 'game/Game-Ranking.html' , context = ctx)
