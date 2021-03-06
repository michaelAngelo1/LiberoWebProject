# Generated by Django 2.2.24 on 2021-10-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_detailstsprharian'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailSTSPRHarianBahan',
            fields=[
                ('Kode', models.IntegerField(db_column='Kode', primary_key=True, serialize=False)),
                ('STSPRH', models.CharField(blank=True, db_column='STSPRH', max_length=10, null=True)),
                ('Teknisi', models.CharField(blank=True, db_column='Teknisi', max_length=10, null=True)),
                ('Satuan', models.CharField(blank=True, db_column='Satuan', max_length=50, null=True)),
                ('Qty', models.IntegerField(blank=True, db_column='Qty', null=True)),
            ],
            options={
                'db_table': 'DetailSTSPRHarianBahan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailSTSPRHarianTeknisi',
            fields=[
                ('Kode', models.IntegerField(db_column='Kode', primary_key=True, serialize=False)),
                ('STSPRH', models.CharField(blank=True, db_column='STSPRH', max_length=10, null=True)),
                ('Teknisi', models.CharField(blank=True, db_column='Teknisi', max_length=10, null=True)),
                ('JobOrder', models.CharField(blank=True, db_column='JobOrder', max_length=10, null=True)),
            ],
            options={
                'db_table': 'DetailSTSPRHarianTeknisi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailSTSPRPIn',
            fields=[
                ('Kode', models.IntegerField(db_column='Kode', primary_key=True, serialize=False)),
                ('Perlengkapan', models.CharField(blank=True, db_column='Perlengkapan', max_length=10, null=True)),
                ('Tanggal', models.DateTimeField(blank=True, db_column='Tanggal', null=True)),
            ],
            options={
                'db_table': 'DetailSTSPRIn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailSTSPRPOut',
            fields=[
                ('Kode', models.IntegerField(db_column='Kode', primary_key=True, serialize=False)),
                ('Perlengkapan', models.CharField(blank=True, db_column='Perlengkapan', max_length=10, null=True)),
                ('Tanggal', models.DateTimeField(blank=True, db_column='Tanggal', null=True)),
            ],
            options={
                'db_table': 'DetailSTSPROut',
                'managed': False,
            },
        ),
    ]
