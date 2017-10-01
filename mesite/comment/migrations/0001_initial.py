# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('email', models.EmailField(max_length=255, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('url', models.URLField(blank=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe4\xb8\xbb\xe9\xa1\xb5')),
                ('text', models.TextField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
        ),
    ]
