# Generated by Django 4.0.4 on 2022-04-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.AddField(
            model_name='room',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='topics', to='base.topic'),
        ),
    ]