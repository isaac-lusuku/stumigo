# Generated by Django 4.2.5 on 2023-11-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_user_date_joined_remove_user_followers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_superuser',
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
