# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=2083)),
                ('title', models.CharField(max_length=2000)),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to='signups.User')),
            ],
        ),
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bid_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('win', models.BooleanField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(to='auctions.Article')),
                ('bidder', models.ForeignKey(to='signups.User')),
            ],
        ),
    ]
