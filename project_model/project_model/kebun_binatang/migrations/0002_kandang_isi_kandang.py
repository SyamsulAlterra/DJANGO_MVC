# Generated by Django 2.2.3 on 2019-07-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kebun_binatang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kandang',
            name='isi_kandang',
            field=models.TextField(default='Hewan'),
        ),
    ]