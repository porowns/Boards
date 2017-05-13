# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'GENERAL', max_length=20, choices=[(b'MATH', b'MATH'), (b'SCIENCE', b'SCIENCE'), (b'HISTORY', b'HISTORY'), (b'GENERAL', b'GENERAL')])),
            ],
        ),
        migrations.AlterField(
            model_name='board',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='app.Category', null=True),
        ),
    ]
