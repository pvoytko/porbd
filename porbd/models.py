# -*- coding: utf-8 -*-

from django.db import models

# Чтобы в дебаг-репортах было видно ID.
class PorBdModel(models.Model):

    class Meta:
        abstract=True

    def __str__(self):
        return "{0} #{1}".format(super(PorBdModel, self).__str__(), self.id)


# Проект
class Project(PorBdModel):

    # Статус
    STATE_CHOICES = (
        ('current', u'текущий'),
        ('draft', u'черновик'),
        ('archive', u'архив'),
    )
    state = models.CharField(max_length=10, choices=STATE_CHOICES, verbose_name=u'Статус')

    # Название полное и короткое
    name = models.CharField(max_length=256, verbose_name=u'Название полное')
    name_short = models.CharField(max_length=56, verbose_name=u'Название короткое')

    # Дата начала, сдачи план, сдачи факт
    date_begin = models.DateField(verbose_name=u'Дата начала')
    date_end_plan = models.DateField(verbose_name=u'Дата сдачи план')
    date_end_fact = models.DateField(verbose_name=u'Дата сдачи факт')

    class Meta:
        verbose_name = u'Проект'
        verbose_name_plural = u'Проекты'
