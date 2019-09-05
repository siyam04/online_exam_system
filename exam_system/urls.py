from django.urls import path

from .views import (

    all_questions,
    question_details,
    exam_details,

)


app_name = 'exam_system'


urlpatterns = [

    path('all_questions/', all_questions, name='all_questions'),

    path('question_details/<int:id>/', question_details, name='question_details'),

    path('exam_details/<int:id>/', exam_details, name='exam_details'),

    # path('profile_create/', profile_create, name='profile_create'),
    #
    #
    # path('profile_edit/', profile_edit, name='profile_edit'),

]


