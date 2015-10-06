# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accordion',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
                ('index', models.PositiveIntegerField(help_text='index of element that should be opened on page load (leave it empty if none of itemes should be opened), zero is the first item', null=True, verbose_name='index', blank=True)),
                ('grouping', models.BooleanField(default=True, help_text='only one can be opened at a time (true) or every entry can be opened individually (false)', verbose_name='grouping')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AccordionItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
