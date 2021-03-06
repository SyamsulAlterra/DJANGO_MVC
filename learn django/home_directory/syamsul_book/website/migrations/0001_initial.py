# Generated by Django 2.2.3 on 2019-07-24 13:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('join_date', models.DateField(verbose_name=datetime.datetime(2019, 7, 24, 13, 13, 6, 222603, tzinfo=utc))),
            ],
        ),
    ]
