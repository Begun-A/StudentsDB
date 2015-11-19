# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20151103_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthJournal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430')),
                ('present_day_1', models.BooleanField(default=False)),
                ('present_day_2', models.BooleanField(default=False)),
                ('present_day_3', models.BooleanField(default=False)),
                ('present_day_4', models.BooleanField(default=False)),
                ('present_day_5', models.BooleanField(default=False)),
                ('present_day_6', models.BooleanField(default=False)),
                ('present_day_7', models.BooleanField(default=False)),
                ('present_day_8', models.BooleanField(default=False)),
                ('present_day_9', models.BooleanField(default=False)),
                ('present_day_10', models.BooleanField(default=False)),
                ('present_day_11', models.BooleanField(default=False)),
                ('present_day_12', models.BooleanField(default=False)),
                ('present_day_13', models.BooleanField(default=False)),
                ('present_day_14', models.BooleanField(default=False)),
                ('present_day_15', models.BooleanField(default=False)),
                ('present_day_16', models.BooleanField(default=False)),
                ('present_day_17', models.BooleanField(default=False)),
                ('present_day_18', models.BooleanField(default=False)),
                ('present_day_19', models.BooleanField(default=False)),
                ('present_day_20', models.BooleanField(default=False)),
                ('present_day_21', models.BooleanField(default=False)),
                ('present_day_22', models.BooleanField(default=False)),
                ('present_day_23', models.BooleanField(default=False)),
                ('present_day_24', models.BooleanField(default=False)),
                ('present_day_25', models.BooleanField(default=False)),
                ('present_day_26', models.BooleanField(default=False)),
                ('present_day_27', models.BooleanField(default=False)),
                ('present_day_28', models.BooleanField(default=False)),
                ('present_day_29', models.BooleanField(default=False)),
                ('present_day_30', models.BooleanField(default=False)),
                ('present_day_31', models.BooleanField(default=False)),
                ('student', models.ForeignKey(unique_for_month=b'date', verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student', null=True)),
            ],
            options={
                'verbose_name': '\u041c\u0456\u0441\u044f\u0447\u043d\u0438\u0439 \u0416\u0443\u0440\u043d\u0430\u043b',
                'verbose_name_plural': '\u041c\u0456\u0441\u044f\u0447\u043d\u0456 \u0416\u0443\u0440\u043d\u0430\u043b\u0438',
            },
        ),
        migrations.RemoveField(
            model_name='journal',
            name='student',
        ),
        migrations.DeleteModel(
            name='Journal',
        ),
    ]
