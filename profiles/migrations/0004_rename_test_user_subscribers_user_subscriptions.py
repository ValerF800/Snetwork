# Generated by Django 4.1 on 2024-11-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_user_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='test',
            new_name='subscribers',
        ),
        migrations.AddField(
            model_name='user',
            name='subscriptions',
            field=models.JSONField(null=True),
        ),
    ]