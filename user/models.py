from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)

class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_games')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_users')
    is_active = models.BooleanField(default=True)

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='cards')
    number = models.IntegerField()

class GameResult(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='result')
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='wins')
    loser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='losses')
    score_won = models.IntegerField()
    score_lost = models.IntegerField()

class Ranking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ranking')
    score_total = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)