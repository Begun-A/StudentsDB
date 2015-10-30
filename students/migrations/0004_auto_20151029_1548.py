# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20151029_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('notes', models.TextField(verbose_name='\u041d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True)),
                ('leader', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='students.Student', verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u0430',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u0438',
            },
        ),
        migrations.RemoveField(
            model_name='groups',
            name='leader',
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
        migrations.AddField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0413\u0440\u0443\u043f\u0430', to='students.Group', null=True),
        ),
    ]
