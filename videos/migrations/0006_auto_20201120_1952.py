# Generated by Django 3.1 on 2020-11-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20201120_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
