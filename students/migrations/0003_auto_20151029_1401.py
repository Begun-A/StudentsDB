# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20151028_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('number_students', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0456\u0432')),
                ('notes', models.TextField(verbose_name='\u041d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u0430',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u0438',
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.TextField(verbose_name='\u041d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.IntegerField(verbose_name='\u2116 \u0421\u0442\u0443\u0434\u0435\u043d\u0441\u0442\u0441\u044c\u043a\u043e\u0433\u043e \u0411\u0456\u043b\u0435\u0442\u0443'),
        ),
        migrations.AddField(
            model_name='groups',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='students.Student', verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430'),
        ),
    ]
