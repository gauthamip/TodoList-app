# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='list_id',
            new_name='listid',
        ),
    ]