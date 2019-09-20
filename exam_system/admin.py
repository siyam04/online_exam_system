from django.contrib import admin

from .models import Questions


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'name', 'option_1', 'option_2', 'option_3', 'option_4',
                    'correct_answer', 'start_time', 'end_time', 'time_length', 'date']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Questions, QuestionsAdmin)

