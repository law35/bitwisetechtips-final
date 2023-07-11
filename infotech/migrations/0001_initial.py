# Generated by Django 2.0.13 on 2021-05-15 05:44

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ITImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='infotech/images')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('uploader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='ITPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='infotech/thumbnails')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('metakeywords', ckeditor.fields.RichTextField(null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
