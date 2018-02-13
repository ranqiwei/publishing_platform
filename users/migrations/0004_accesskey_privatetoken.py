# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-06 15:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180124_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name=b'AccessKeyID')),
                ('secret', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=b'AccessKeySecret')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_key', to=settings.AUTH_USER_MODEL, verbose_name=b'User')),
            ],
        ),
        migrations.CreateModel(
            name='PrivateToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Private Token',
            },
        ),
    ]