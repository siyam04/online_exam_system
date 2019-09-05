from django.contrib import admin

from .models import Questions


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'name', 'option_1', 'option_2', 'option_3', 'option_4',
                    'correct_answer', 'start_time', 'end_time', 'time_length', 'date']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']


# class ExamProcessAdmin(admin.ModelAdmin):
#     list_display = ['id', 'exam_user', 'exam_name', 'exam_question_set', 'start_time', 'end_time',
#                     'date', 'active_status', 'time_length']
#
#     list_display_links = ['exam_name']
#     list_filter = ['exam_name']
#     search_fields = ['exam_name', 'exam_user']
#     list_editable = ['active_status']


admin.site.register(Questions, QuestionsAdmin)
# admin.site.register(ExamProcess, ExamProcessAdmin)

