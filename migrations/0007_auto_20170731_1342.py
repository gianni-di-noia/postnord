# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_nord', '0006_attachment_mimetype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailtemplate',
            options={'ordering': ['name'], 'verbose_name': 'Email Template', 'verbose_name_plural': 'Email Templates'},
        ),
    ]
