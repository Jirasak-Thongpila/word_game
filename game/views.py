from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import random
from .models import Word, GameSession

# Create your views here.

def index(request):
    return render(request, 'game/index.html')

@require_http_methods(["GET"])
def get_random_word(request):
    try:
        language = request.GET.get('language', 'th')
        difficulty = int(request.GET.get('difficulty', 1))

        # Get random word from database
        words = Word.objects.filter(language=language, difficulty=difficulty)
        if not words.exists():
            return JsonResponse({
                'success': False,
                'error': f'ไม่มีคำศัพท์ในฐานข้อมูลสำหรับภาษา {language} ระดับ {difficulty}'
            })

        word = random.choice(words).word

        # Shuffle letters
        letters = list(word)
        shuffled_letters = letters.copy()
        while shuffled_letters == letters:
            random.shuffle(shuffled_letters)

        return JsonResponse({
            'success': True,
            'word': word,
            'shuffled_letters': shuffled_letters
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

@csrf_exempt
@require_http_methods(["POST"])
def check_word(request):
    try:
        data = json.loads(request.body)
        user_word = data.get('user_word', '').lower()
        correct_word = data.get('correct_word', '').lower()

        is_correct = user_word == correct_word

        return JsonResponse({
            'success': True,
            'is_correct': is_correct
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

@csrf_exempt
@require_http_methods(["POST"])
def save_score(request):
    try:
        data = json.loads(request.body)
        session_id = data.get('session_id')
        score = data.get('score', 0)
        words_completed = data.get('words_completed', 0)

        if not session_id:
            return JsonResponse({
                'success': False,
                'error': 'session_id is required'
            })

        # Update or create game session
        session, created = GameSession.objects.update_or_create(
            session_id=session_id,
            defaults={
                'score': score,
                'words_completed': words_completed
            }
        )

        return JsonResponse({
            'success': True,
            'session_id': session.session_id,
            'score': session.score
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
