# Generated by Django 4.1 on 2024-11-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.JSONField(null=True),
        ),
    ]
