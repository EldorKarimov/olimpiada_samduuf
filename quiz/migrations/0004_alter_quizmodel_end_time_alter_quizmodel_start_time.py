# Generated by Django 5.0 on 2023-12-23 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quizmodel_end_time_quizmodel_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
