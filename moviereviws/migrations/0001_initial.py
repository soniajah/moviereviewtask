# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-24 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('ReviewTitle', models.CharField(max_length=50)),
                ('ReviewContent', models.TextField()),
                ('MovieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviereviws.Movies')),
            ],
        ),
    ]
