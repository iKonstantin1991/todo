# Generated by Django 3.0.5 on 2021-11-14 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_responsible', to=settings.AUTH_USER_MODEL),
        ),
    ]
