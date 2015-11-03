# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_resalt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resalt',
            options={'verbose_name': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442', 'verbose_name_plural': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0438'},
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430'),
        ),
    ]
