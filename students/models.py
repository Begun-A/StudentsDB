# -*- coding: utf-8 -*-

from django.db import models
# Create your models here.


class Student(models.Model):
    """Srudents Model"""
    class Meta(object):
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенти'

    def __unicode__(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім\'я"
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Прізвище'
    )

    midle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u'По-батькові',
        default=''
    )

    birthday = models.DateField(
        blank=False,
        verbose_name=u'Дата народження',
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name=u'Фото студента',
        null=True
    )

    ticket = models.IntegerField(
        blank=False,
        verbose_name='№ Студенстського Білету'
    )

    notes = models.TextField(
        blank=True,
        verbose_name='Нотатки'
    )

