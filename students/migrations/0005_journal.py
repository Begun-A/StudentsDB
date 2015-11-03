# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20151029_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430')),
                ('check', models.BooleanField(verbose_name='\u041f\u0440\u0438\u0441\u0443\u0442\u043d\u0456\u0441\u0442\u044c')),
                ('student', models.ForeignKey(verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student', null=True)),
            ],
            options={
                'verbose_name': '\u0416\u0443\u0440\u043d\u0430\u043b',
                'verbose_name_plural': '\u0416\u0443\u0440\u043d\u0430\u043b',
            },
        ),
    ]
