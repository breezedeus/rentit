# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Outorder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=100, verbose_name=b'Item name')),
                ('price', models.FloatField()),
                ('address', models.CharField(max_length=100, null=True, verbose_name=b'Address to get the object')),
                ('description', models.CharField(default=b'The creator is so lazy.', max_length=5000)),
                ('borrower_id', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateTimeField(verbose_name=b'date the item may rent out')),
                ('end_date', models.DateTimeField(verbose_name=b'date the item may be sent back')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField(null=True)),
                ('description', models.CharField(default=b'I want to rent it.', max_length=5000)),
                ('start_date', models.DateTimeField(verbose_name=b'date the user may want to rent out')),
                ('end_date', models.DateTimeField(verbose_name=b'date the user may want to sent the item back')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('rating', models.PositiveSmallIntegerField(default=3)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('outorder', models.ForeignKey(to='rentout.Outorder')),
            ],
        ),
    ]
