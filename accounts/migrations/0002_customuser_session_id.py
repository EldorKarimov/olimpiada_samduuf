# Generated by Django 5.0 on 2023-12-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='session_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
