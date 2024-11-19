# Generated by Django 4.1 on 2024-11-19 08:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_rename_test_user_subscribers_user_subscriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='subscribers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subscriptions',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profiles/%Y/%m/%d'),
        ),
    ]