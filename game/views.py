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

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('user:login')  # 로그인 페이지로 리디렉션
    return render(request, 'game/dashboard.html')

@login_required
def game_start_view(request):
    return render(request, 'game_start.html')

@login_required
def game_history_view(request):
    return render(request, 'game_history.html')

