# Generated by Django 2.2.3 on 2019-07-24 14:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190724_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orang',
            name='birth_date',
        ),
        migrations.AlterField(
            model_name='orang',
            name='join_date',
            field=models.DateField(verbose_name=datetime.datetime(2019, 7, 24, 14, 11, 0, 959282, tzinfo=utc)),
        ),
    ]