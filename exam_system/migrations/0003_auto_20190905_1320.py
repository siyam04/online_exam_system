# Generated by Django 2.2.1 on 2019-09-05 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_system', '0002_auto_20190905_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examprocess',
            name='exam_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_profile', to='custom_users.Profile'),
        ),
    ]