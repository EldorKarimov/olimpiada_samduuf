# Generated by Django 5.0 on 2023-12-23 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_quizmodel_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 5, 56, 21, 298362, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 5, 56, 42, 755219, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]