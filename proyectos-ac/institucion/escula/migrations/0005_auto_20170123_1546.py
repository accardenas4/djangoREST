# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escula', '0004_auto_20170123_1545'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alumno',
            new_name='Materia',
        ),
    ]
