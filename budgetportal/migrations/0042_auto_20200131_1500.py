# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-31 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("budgetportal", "0041_auto_20191129_1715"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="irmsnapshot", unique_together=set([("financial_year", "quarter")]),
        ),
    ]
