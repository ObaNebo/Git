# Generated by Django 5.1.4 on 2024-12-16 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='trask',
            field=models.TextField(default=2, verbose_name='Описание задачи'),
            preserve_default=False,
        ),
    ]
