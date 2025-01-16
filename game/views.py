from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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