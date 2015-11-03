# -*- coding: utf-8 -*-

from django.db import models

class Exam(models.Model):
    """ Exam model"""
    class Meta(object):
        verbose_name = u'Екзамен'
        verbose_name_plural = u'Екзамени'

    lesson = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name=u'Предмет'
    )

    date = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name=u'Дата проведення'
    )

    teacher = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name=u'Викладач'
    )

    exam_group = models.ForeignKey('Group',
        blank=False,
        null=True,
        verbose_name=u'Група',
        on_delete=models.CASCADE
    )

    def __unicode__(self):
        return u'{0} {1}'.format(self.lesson, self.exam_group)