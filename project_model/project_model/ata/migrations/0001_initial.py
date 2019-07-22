# Generated by Django 2.2.3 on 2019-07-22 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Orang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('nomor_telepon', models.IntegerField(verbose_name='Nomor telepon')),
            ],
        ),
        migrations.CreateModel(
            name='Direksi',
            fields=[
                ('orang_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ata.Orang')),
                ('jabatan', models.CharField(max_length=200)),
            ],
            bases=('ata.orang',),
        ),
        migrations.CreateModel(
            name='LiveCode',
            fields=[
                ('materi_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ata.Materi')),
                ('tanggal_pelaksanaan', models.DateTimeField(verbose_name='Tanggal Pelaksanaan')),
            ],
            bases=('ata.materi',),
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('materi_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ata.Materi')),
                ('jadwal_mulai', models.DateTimeField(verbose_name='Jadwal mulai')),
                ('jadwal_berakhir', models.DateTimeField(verbose_name='Jadwal berakhir')),
            ],
            bases=('ata.materi',),
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('orang_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ata.Orang')),
                ('nomor_absen', models.IntegerField(verbose_name='Nomor absen')),
                ('nilai_rata_rata', models.IntegerField(verbose_name='Nilai rata-rata')),
            ],
            bases=('ata.orang',),
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('orang_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ata.Orang')),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ata.MataPelajaran')),
            ],
            bases=('ata.orang',),
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('materi_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ata.Materi')),
                ('banyak_soal', models.IntegerField(verbose_name='Banyak soal')),
                ('bobot_nilai', models.IntegerField(verbose_name='Bobot nilai')),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ata.MataPelajaran')),
            ],
            bases=('ata.materi',),
        ),
    ]