# Generated by Django 2.0.13 on 2021-06-13 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linux', '0002_auto_20210523_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='linuxposts',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='linux/files'),
        ),
    ]
