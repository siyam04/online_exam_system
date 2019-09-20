from django.db import models

from custom_users.models import Profile


class Questions(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')

    name = models.CharField(max_length=150)
    option_1 = models.CharField(max_length=50)
    option_2 = models.CharField(max_length=50)
    option_3 = models.CharField(max_length=50)
    option_4 = models.CharField(max_length=50)

    start_time = models.TimeField()
    end_time = models.TimeField()

    date = models.DateField(auto_now=True)

    @property
    def time_length(self):
        if self.start_time < self.end_time:
            valid = True
            return valid

    @property
    def correct_answer(self):
        answer = self.option_4
        return answer

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.name




