# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

store_types = (
    ('R', 'Restaurants'),
    ('S', 'Stationary'),
    ('SM', 'SuperMarkets'),
    ('SS', 'Salon & Spa'),
    ('P', 'Pharmacies'),
    ('AS', 'Apparel Stores'),
    ('H', 'Hardware'),
)

payment_types = (
    ('PT', 'PayTm'),
    ('UPI', 'UPI'),
    ('DC', 'Debit Card')
)


class Store(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    store_type = models.CharField(max_length=255, blank=True, null=True, choices=store_types)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    lat = models.DecimalField(decimal_places=20, max_digits=25)
    long = models.DecimalField(decimal_places=20, max_digits=25)
    vpa = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __unicode__(self):
        return str(self.name)


class PaymentType(models.Model):
    store = models.ForeignKey(Store, related_name='p_type')
    payment_type = models.CharField(max_length=255, blank=True, null=True, choices=payment_types)

    def __unicode__(self):
        return str(self.payment_type)
