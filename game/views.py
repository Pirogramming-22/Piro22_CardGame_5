from django.shortcuts import render, redirect
from .models import Game
from django.conf import settings  # settings.AUTH_USER_MODEL 사용
from django.db.models import Q

import random
from user.models import CustomUser
from django.http import HttpResponseBadRequest
from django.contrib.auth import get_user_model

# Create your views here.

def gameHistory(request): #1
    if not request.user.is_authenticated:
        return redirect('user:login')

    games = Game.objects.filter(Q(player1=request.user) | Q(player2=request.user))
    user = request.user
    ctx = {
        'games': games,
        'user': user,
    }
    return render(request, 'game/game-history.html', context=ctx)


def delete_game(request, pk): #2
    game = Game.objects.get(id=pk)
    game.delete()
    return redirect('game:gameHistory')

def gameRankingTop3(request): #3
    if not request.user.is_authenticated:
        return redirect('user:login')
    User = get_user_model()  # 커스터마이즈된 유저 모델 호환
    users = User.objects.all()
    top3_users = users.order_by('-point')[:3]

    ctx = {
        'top3_users': top3_users,
    }
    return render(request, 'game/Game-Ranking-Top3.html', context=ctx)

def dashboard_view(request): #4
    user = request.user  # 현재 로그인한 사용자
    username = user.username  # OAuth 연결 여부와 상관없이 사용자 이름을 사용
    return render(request, 'game/dashboard.html', {'username': username})

def base(request): #5
    return render(request, 'main.html')



def game_start_view(request): #6
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

def attack(request, game_pk): #7
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

def game_detail(request, game_pk): #8
    game = Game.objects.get(pk=game_pk)
    return render(request, 'game/game_detail.html', {'match': game})