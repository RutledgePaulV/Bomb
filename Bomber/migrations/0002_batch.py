# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bomber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('size', models.PositiveIntegerField()),
                ('complete', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
