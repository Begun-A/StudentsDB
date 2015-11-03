# -*- coding: utf-8 -*-

from django.db import models


class Journal(models.Model):
    """Journal Model"""
    class Meta(object):
        verbose_name = u'Журнал'
        verbose_name_plural = u'Журнал'

    student = models.ForeignKey('Student',
        blank=False,
        null=True,
        verbose_name=u'Студент',
        on_delete=models.CASCADE
                                 )
    data = models.DateField(
        blank=False,
        null=True,
        verbose_name=u'Дата'
    )

    check = models.BooleanField(
        blank=False,
        null=False,
        verbose_name=u'Присутність'
    )

    def __unicode__(self):
        return "{}{}{}".format()

