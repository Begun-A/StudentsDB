# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20151102_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resalt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.IntegerField(null=True, verbose_name='\u041e\u0446\u0456\u043d\u043a\u0430', blank=True)),
                ('resalt_examen', models.ForeignKey(verbose_name='\u0415\u043a\u0437\u0430\u043c\u0435\u043d', to='students.Exam', null=True)),
                ('resalt_student', models.ForeignKey(verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student', null=True)),
            ],
            options={
                'verbose_name': ('\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442',),
                'verbose_name_plural': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0438',
            },
        ),
    ]
