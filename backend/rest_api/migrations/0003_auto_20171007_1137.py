# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20171007_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(blank=True, choices=[('PT', 'PayTm'), ('UPI', 'UPI'), ('DC', 'Debit Card')], max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='store',
            name='payment_type',
        ),
        migrations.AddField(
            model_name='paymenttype',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.Store'),
        ),
    ]
