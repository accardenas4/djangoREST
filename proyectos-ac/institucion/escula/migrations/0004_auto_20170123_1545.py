# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escula', '0003_auto_20170123_1542'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Materia',
            new_name='Alumno',
        ),
    ]
