# -*- coding: utf-8 -*-

from django.db import models

class Resalt(models.Model):
    """Resalt exam model"""
    class Meta(object):
        verbose_name = u'Результат'
        verbose_name_plural = u'Результати'

    resalt_examen = models.ForeignKey('Exam',
        blank=False,
        null=True,
        verbose_name=u'Екзамен',
        on_delete=models.CASCADE
    )

    resalt_student = models.ForeignKey('Student',
        blank=False,
        null=True,
        verbose_name=u'Студент',
        on_delete=models.CASCADE
    )

    mark = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=u'Оцінка'
    )

    def __unicode__(self):
        return u'{0} {1}'.format(self.resalt_student, self.resalt_examen)


