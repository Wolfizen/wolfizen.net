# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShowVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_ip', models.GenericIPAddressField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='wolfizen_net.Show')),
            ],
        ),
    ]
