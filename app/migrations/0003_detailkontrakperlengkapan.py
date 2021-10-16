# Generated by Django 2.2.24 on 2021-10-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_detailkontrakbahan'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailKontrakPerlengkapan',
            fields=[
                ('kode', models.IntegerField(db_column='kode', primary_key=True, serialize=False)),
                ('Perlengkapan', models.CharField(blank=True, db_column='Perlengkapan', max_length=10, null=True)),
                ('Nominal', models.DecimalField(blank=True, db_column='Nominal', decimal_places=4, max_digits=12, null=True)),
                ('Qty', models.IntegerField(blank=True, db_column='Qty', null=True)),
            ],
            options={
                'db_table': 'DetailKontrakPerlengkapan',
                'managed': False,
            },
        ),
    ]