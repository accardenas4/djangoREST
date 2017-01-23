# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escula', '0002_auto_20170123_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='apellido',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='materia',
            name='cedula',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='materia',
            name='ciudad',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='materia',
            name='provincia',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
