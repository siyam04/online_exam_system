from django.db import models

from custom_users.models import Profile


class Questions(models.Model):
    name = models.CharField(max_length=150)
    option_1 = models.CharField(max_length=50)
    option_2 = models.CharField(max_length=50)
    option_3 = models.CharField(max_length=50)
    option_4 = models.CharField(max_length=50)

    @property
    def correct_answer(self):
        answer = self.option_4
        return answer

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.name


class ExamProcess(models.Model):

    EXAM_NAME = (
        ('Exam 1', 'Exam 1'),
        ('Exam 2', 'Exam 2'),
    )

    exam_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='exam_profile')
    exam_name = models.CharField(max_length=20, choices=EXAM_NAME)
    exam_question_set = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='exam_question')
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField(auto_now=True)
    active_status = models.BooleanField(default=False)

    @property
    def time_length(self):
        if self.start_time < self.end_time:
            valid = True
            return valid

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'ExamProcess'

    def __str__(self):
        return self.exam_name


