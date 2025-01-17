from django.shortcuts import render, redirect, get_object_or_404
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




def attack(request):
    if not request.user.is_authenticated:
        return redirect('user:login')
    game = request.POST.get('game')

    if request.method == 'POST':
        selected_card = int(request.POST.get('card'))  
        if not selected_card:
            return HttpResponseBadRequest("카드를 선택해야 합니다.")

        selected_card = int(selected_card)  

        defender_id = int(request.POST.get('defender'))  

        defender = CustomUser.objects.get(pk=defender_id)

        if game.player1 == request.user:
            game.player1_choice = selected_card
            if game.player2 is None:
                game.player2 = defender
        elif game.player2 == request.user:
            game.player2_choice = selected_card

        game.save()

        game.determine_winner()

        result = "무승부"
        if game.winner:
            result = 'win' if game.winner == game.player1 else 'lose'

        if game.winner: 
            status = 'finished'
        elif game.player2 == defender:  
            status = 'counterattack'
        else:  
            status = 'in_progress'
            
        games = {
            'match': {
                'attacker': game.player1.username, 
                'defender': game.player2.username,  
                'attacker_card': game.player1_choice,  
                'defender_card': game.player2_choice,  
                'result': result,  
                'status': status,
            }
        }
        return render('game/game_history.html', context=games)  
    return HttpResponseBadRequest("잘못된 요청입니다.")

def counterattack(request, game_pk):
    if not request.user.is_authenticated:
        return redirect('user:login')  
    
    game = get_object_or_404(Game, pk=game_pk)  

    if request.method == 'POST':
        selected_card = request.POST.get('card')  

        if not selected_card:
            return HttpResponseBadRequest("카드를 선택해야 합니다.")

        selected_card = int(selected_card)  

        if game.player1 == request.user:
            game.player1_choice = selected_card 
        elif game.player2 == request.user:
            game.player2_choice = selected_card  
        else:
            return HttpResponseBadRequest("현재 게임에 참여하지 않은 사용자입니다.")

        game.save()  
        game.determine_winner()

        # 게임 결과 기록을 저장
        result = "무승부"
        if game.winner:
            result = 'win' if game.winner == game.player1 else 'lose'

        if game.winner: 
            status = 'finished'
        result_data = {
            'match': {
                'number': game.pk,  
                'attacker': game.player1.username, 
                'defender': game.player2.username,  
                'attacker_card': game.player1_choice,  
                'defender_card': game.player2_choice,  
                'result': result,  
                'status': status,
            }
        }
        return render(request, 'game/game_detail.html', context=result_data) 
    return HttpResponseBadRequest("잘못된 요청입니다.")

def game_detail(request, pk): #8
    game = Game.objects.get(id=pk)
    return render(request, 'game/game_detail.html', {'match': game})

def go_counterattack(request, pk):
    if not request.user.is_authenticated:
        return redirect('user:login')   
    
    game = get_object_or_404(Game, pk=pk) 
    return render(request, 'game/counter_attack.html', {'game':game})

def counterattack_view(request, pk):
   if not request.user.is_authenticated:
        return redirect('user:login')
   
   game = get_object_or_404(Game, pk=pk) 
   
   if request.method == 'POST':
        cards = random.sample(range(1, 11), 5)  
        selected_card = request.POST.get('card')  
        defender = game.player2 if game.player1 == request.user else game.player1 
        game.player1_choice = selected_card if game.player1 == request.user else game.player1_choice
        game.player2_choice = selected_card if game.player2 == request.user else game.player2_choice
        game.save()
        game.determine_winner()
        return render(request, 'game/game_detail.html', {'game': game, 'cards': cards})