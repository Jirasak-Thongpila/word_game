# game/models.py
from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=20)
    language = models.CharField(max_length=10, choices=[('th', 'Thai'), ('en', 'English')])
    difficulty = models.IntegerField(default=1)  # 1=Easy, 2=Medium, 3=Hard
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.word} ({self.language})"

class GameSession(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    score = models.IntegerField(default=0)
    words_completed = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Session {self.session_id} - Score: {self.score}"
