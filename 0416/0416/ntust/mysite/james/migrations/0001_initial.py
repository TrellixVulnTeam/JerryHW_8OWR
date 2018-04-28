# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-28 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=5)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Female_Male', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='gender',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='james.Name'),
        ),
        migrations.AddField(
            model_name='birthday',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='james.Name'),
        ),
    ]
