# Generated by Django 4.2.8 on 2023-12-29 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_quizuser_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quizuser',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 10, 12, 7, 289928, tzinfo=datetime.timezone.utc)),
        ),
    ]
