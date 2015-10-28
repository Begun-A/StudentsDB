# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name="\u0406\u043c'\u044f")),
                ('last_name', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
                ('midle_name', models.CharField(default=b'', max_length=256, verbose_name='\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f')),
                ('foro', models.ImageField(upload_to=b'', null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe \xd1\x81\xd1\x82\xd1\x83\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0', blank=True)),
                ('ticket', models.IntegerField(verbose_name=b'\xe2\x84\x96 \xd0\xa1\xd1\x82\xd1\x83\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x81\xd1\x82\xd1\x81\xd1\x8c\xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe \xd0\x91\xd1\x96\xd0\xbb\xd0\xb5\xd1\x82\xd1\x83')),
                ('notes', models.TextField(verbose_name=b'\xd0\x9d\xd0\xbe\xd1\x82\xd0\xb0\xd1\x82\xd0\xba\xd0\xb8', blank=True)),
            ],
        ),
    ]
