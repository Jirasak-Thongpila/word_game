# game/admin.py
from django.contrib import admin
from .models import Word, GameSession

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'language', 'difficulty', 'created_at')
    list_filter = ('language', 'difficulty')
    search_fields = ('word',)
    ordering = ('language', 'difficulty', 'word')

    fieldsets = (
        ('ข้อมูลคำศัพท์', {
            'fields': ('word', 'language', 'difficulty')
        }),
    )

@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'score', 'words_completed', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('session_id',)
    readonly_fields = ('session_id', 'created_at', 'updated_at')
    ordering = ('-score', '-updated_at')

    fieldsets = (
        ('ข้อมูลเซสชัน', {
            'fields': ('session_id', 'created_at', 'updated_at')
        }),
        ('คะแนน', {
            'fields': ('score', 'words_completed')
        }),
    )
