from django.conf import settings  # settings.AUTH_USER_MODEL 사용
from django.db import models

class Game(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    player1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='games_as_player1', on_delete=models.CASCADE) # 대결신청을 보내는 플레이어
    player2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='games_as_player2', on_delete=models.CASCADE, null=True, blank=True)
    # 플레이어 기본적으로 두명

    player1_choice = models.IntegerField(null=True, blank=True)  # 1~5 중 하나 선택
    player2_choice = models.IntegerField(null=True, blank=True)  # 1~5 중 하나 선택

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')

    winner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='games_won', on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def determine_winner(self):
        if self.player1_choice is not None and self.player2_choice is not None:  # 두 개의 응답이 모두 None이 아닐 때
            if self.player1_choice > self.player2_choice:
                self.winner = self.player1
            elif self.player1_choice < self.player2_choice:
                self.winner = self.player2
            else:
                self.winner = None  # 무승부
            self.status = 'completed'
            self.save()