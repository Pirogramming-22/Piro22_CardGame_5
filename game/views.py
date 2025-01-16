from django.shortcuts import render, redirect
from .models import Game
from django.conf import settings  # settings.AUTH_USER_MODEL 사용
from django.db.models import Q
import random
from user.models import CustomUser
from django.http import HttpResponseBadRequest

# Create your views here.

def delete_game(request, pk):
    game = Game.objects.get(id=pk)
    game.delete()
    return redirect('game:gameHistory')

def gameRankingTop3(request):
    if not request.user.is_authenticated:
        return redirect('user:login')

    User = settings.AUTH_USER_MODEL  # 커스터마이즈된 유저 모델 호환
    users = User.objects.all()
    top3_users = users.order_by('-win_count')[:3]
    ctx = {
        'top3_users': top3_users,
    }
    return render(request, 'game/Game-Ranking-Top3.html', context=ctx)

def gameRanking(request):
    if not request.user.is_authenticated:
        return redirect('user:login')

    User = settings.AUTH_USER_MODEL  # 커스터마이즈된 유저 모델 호환
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
    game = Game.objects.first()
    if not game:
        game = None
    cards = random.sample(range(1, 11), 5)
    defenders = CustomUser.objects.exclude(id=request.user.id)

    ctx = {
        'cards': cards,  
        'defenders': defenders,
        'game': game,  
    }
    return render(request, 'game/game_start.html', context=ctx)

def game_history_view(request):
    if not request.user.is_authenticated:
        return redirect('user:login')

    return render(request, 'game_history.html')

def attack(request, game_pk):
    if not request.user.is_authenticated:
        return redirect('user:login')
    game = Game.objects.get(pk=game_pk)

    if request.method == 'POST':
        selected_card = int(request.POST.get('card'))  
        defender_id = int(request.POST.get('defender'))  
        
        defender = CustomUser.objects.get(pk=defender_id)

        if game.player1 == request.user:
            game.player1_choice = selected_card
            game.player2 = defender
        elif game.player2 == request.user:
            game.player2_choice = selected_card

        game.save()

        game.determine_winner()

        return redirect('game:gameHistory')  

    return HttpResponseBadRequest("잘못된 요청입니다.")