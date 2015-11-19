# -*- coding: utf-8 -*-

from django.db import models


class MonthJournal(models.Model):
    """Journal Model"""

    class Meta(object):
        verbose_name = u'Місячний Журнал'
        verbose_name_plural = u'Місячні Журнали'

    student = models.ForeignKey('Student',
                                blank=False,
                                null=True,
                                verbose_name=u'Студент',
                                unique_for_month='date',
                                on_delete=models.CASCADE
                                )
    date = models.DateField(
        blank=False,
        null=True,
        verbose_name=u'Дата'
    )

    present_day_1 = models.BooleanField(default=False)
    present_day_2 = models.BooleanField(default=False)
    present_day_3 = models.BooleanField(default=False)
    present_day_4 = models.BooleanField(default=False)
    present_day_5 = models.BooleanField(default=False)
    present_day_6 = models.BooleanField(default=False)
    present_day_7 = models.BooleanField(default=False)
    present_day_8 = models.BooleanField(default=False)
    present_day_9 = models.BooleanField(default=False)
    present_day_10 = models.BooleanField(default=False)
    present_day_11 = models.BooleanField(default=False)
    present_day_12 = models.BooleanField(default=False)
    present_day_13 = models.BooleanField(default=False)
    present_day_14 = models.BooleanField(default=False)
    present_day_15 = models.BooleanField(default=False)
    present_day_16 = models.BooleanField(default=False)
    present_day_17 = models.BooleanField(default=False)
    present_day_18 = models.BooleanField(default=False)
    present_day_19 = models.BooleanField(default=False)
    present_day_20 = models.BooleanField(default=False)
    present_day_21 = models.BooleanField(default=False)
    present_day_22 = models.BooleanField(default=False)
    present_day_23 = models.BooleanField(default=False)
    present_day_24 = models.BooleanField(default=False)
    present_day_25 = models.BooleanField(default=False)
    present_day_26 = models.BooleanField(default=False)
    present_day_27 = models.BooleanField(default=False)
    present_day_28 = models.BooleanField(default=False)
    present_day_29 = models.BooleanField(default=False)
    present_day_30 = models.BooleanField(default=False)
    present_day_31 = models.BooleanField(default=False)

    def __unicode__(self):
        return "{0}{1}{2}".format(self.student.last_name, self.date.month,
                                  self.date.year)
# field = models.BooleanField(default=False)
# for i in range(1,32):
#     setattr(MonthJournal,'present_day_{0}'.format(i),field)