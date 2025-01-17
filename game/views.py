from django.shortcuts import render, redirect
from .models import Game
from django.conf import settings  # settings.AUTH_USER_MODEL 사용
from django.db.models import Q
from django.contrib.auth import get_user_model

# Create your views here.

def gameHistory(request):
    if not request.user.is_authenticated:
        return redirect('user:login')

    games = Game.objects.filter(Q(player1=request.user) | Q(player2=request.user))
    user = request.user
    ctx = {
        'games': games,
        'user': user,
    }
    return render(request, 'game/Game-History.html', context=ctx)

def delete_game(request, pk):
    game = Game.objects.get(id=pk)
    game.delete()
    return redirect('game:gameHistory')

def gameRankingTop3(request):
    if not request.user.is_authenticated:
        return redirect('user:login')

    User = get_user_model()  # 커스터마이즈된 유저 모델 호환
    users = User.objects.all()
    top3_users = users.order_by('-point')[:3]
    ctx = {
        'top3_users': top3_users,
    }
    return render(request, 'game/Game-Ranking-Top3.html', context=ctx)

def gameRanking(request):
    if not request.user.is_authenticated:
        return redirect('user:login')

    User = get_user_model()  # 커스터마이즈된 유저 모델 호환
    users = User.objects.all()
    ctx = {
        'users': users,
    }
    return render(request, 'game/Game-Ranking.html', context=ctx)

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('user:login')  # 로그인 페이지로 리디렉션
    return render(request, 'game/dashboard.html')

def game_start_view(request):
    if not request.user.is_authenticated:
        return redirect('user:login')

    return render(request, 'game_start.html')

def game_history_view(request):
    if not request.user.is_authenticated:
        return redirect('user:login')

    return render(request, 'game_history.html')