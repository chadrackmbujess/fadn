# Generated by Django 5.0.7 on 2024-07-20 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0005_video_name_alter_video_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
    ]
