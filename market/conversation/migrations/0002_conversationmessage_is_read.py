# Generated by Django 5.0.2 on 2024-08-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationmessage',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
