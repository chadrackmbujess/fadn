# Generated by Django 5.0.7 on 2024-07-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0004_video_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
