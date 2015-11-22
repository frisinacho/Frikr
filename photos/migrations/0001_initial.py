# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField()),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('license', models.CharField(max_length=3, choices=[(b'RIG', b'Copyright'), (b'LEF', b'Copyleft'), (b'CC', b'Creative Commons')])),
            ],
        ),
    ]
