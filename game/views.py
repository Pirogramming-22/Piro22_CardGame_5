from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from django.conf import settings  # settings.AUTH_USER_MODEL 사용
from django.db.models import Q
import random
from user.models import CustomUser
from django.http import HttpResponseBadRequest
from django.contrib.auth import get_user_model

import logging

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
    return render(request, 'game/game_history.html', context=ctx)


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


def base(request): #5
    return render(request, 'main.html')

def game_start_view(request):
    if not request.user.is_authenticated:
        return redirect('user:login')
    game = Game.objects.first()
    cards = random.sample(range(1, 11), 5)
    defenders = CustomUser.objects.exclude(id=request.user.id)

    ctx = {
        'cards': cards,  
        'defenders': defenders,
        'game': game,  
    }
    return render(request, 'game/game_start.html', context=ctx)


def create_game(request):
    if request.method == 'POST':
        defender_id = request.POST.get('defender')
        game = Game.objects.create(
            player1 = request.user,
            player2 = CustomUser.objects.get(id=defender_id),
            player1_choice = request.POST.get('card'),
        )
        game.save()
        return redirect('game:gameHistory')
    return HttpResponseBadRequest("잘못된 요청입니다.")

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    point = None
    if game.status == 'completed':
        if game.winner == game.player1:
            point = game.player1_choice - game.player2_choice
        elif game.winner == game.player2:
            point = game.player2_choice - game.player1_choice

    return render(request, 'game/game_detail.html', {
        'match': game,
        'point': point,
    })

def go_counterattack(request, pk): #히스토리에서 -> 카운터 어택으로
    logging.debug("Hello")
    if not request.user.is_authenticated:
        return redirect('user:login')
    game = get_object_or_404(Game, pk=pk)
    cards = random.sample(range(1, 11), 5)

    ctx = {
        'cards': cards,  
        'game': game,  
        'pk': pk,
    }
    return render(request, 'game/counter_attack.html', context=ctx)

def counterattack_view(request, pk): #카드 선택 -> 디테일로로
   if not request.user.is_authenticated:
        return redirect('user:login')

   game = get_object_or_404(Game, pk=pk) 
   if request.method == 'POST':
        cards = random.sample(range(1, 11), 5)  
        selected_card = request.POST.get('card')  

        game.player2_choice = selected_card

        game.save()
        game.determine_winner()
        
        counterattack = {
            'match': game,
            'cards': cards,
        }
        return render(request, 'game/counter_attack.html', counterattack)
   return HttpResponseBadRequest("잘못된 요청입니다.")

from django.http import HttpResponseBadRequest

def before_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('user:login')

    if request.method != 'POST':
        return HttpResponseBadRequest("잘못된 요청입니다.")

    card = request.POST.get('card')
    if card is None:
        return HttpResponseBadRequest("카드 데이터가 없습니다.")

    game = get_object_or_404(Game, pk=pk)
    game.player2_choice = int(card)
    game.status = 'completed'
    game.save()
    game.determine_winner()

    point = abs(game.player1_choice - game.player2_choice)

    return render(request, 'game/game_detail.html', {
        'match': game,
        'point': point,
    })
