# Generated by Django 4.0.4 on 2022-04-27 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_prediction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='user',
        ),
    ]