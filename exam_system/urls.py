from django.urls import path

from .views import (

    all_questions,
    question_details,
    answer_details,
)


app_name = 'exam_system'


urlpatterns = [

    path('all_questions/', all_questions, name='all_questions'),

    path('question_details/<int:id>/', question_details, name='question_details'),

    path('answer_details/<int:id>/', answer_details, name='answer_details'),

]


