# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_auto_20171007_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='rating',
            field=models.FloatField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('PT', 'PayTm'), ('PP', 'PhonePe'), ('M', 'Mobikwik')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_types', to='rest_api.Store'),
        ),
    ]
