# Generated by Django 3.1.7 on 2021-04-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='vimeo_id',
            field=models.CharField(default='1', max_length=32),
        ),
    ]
