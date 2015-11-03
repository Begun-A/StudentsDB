# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_exam_exam_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_group',
            field=models.ForeignKey(verbose_name='\u0413\u0440\u0443\u043f\u0430', to='students.Group', null=True),
        ),
    ]
