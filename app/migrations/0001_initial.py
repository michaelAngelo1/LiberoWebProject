# Generated by Django 2.2.24 on 2021-09-18 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bahan',
            fields=[
                ('Kode', models.CharField(db_column='Kode', max_length=20, primary_key=True, serialize=False)),
                ('Nama', models.CharField(blank=True, db_column='Nama', max_length=250, null=True)),
                ('Tipe', models.CharField(blank=True, db_column='Tipe', max_length=50, null=True)),
                ('Qty', models.IntegerField(blank=True, db_column='Qty', null=True)),
                ('Satuan', models.CharField(blank=True, db_column='Satuan', max_length=10, null=True)),
                ('HargaBeli', models.DecimalField(blank=True, db_column='HargaBeli', decimal_places=4, max_digits=12, null=True)),
                ('HargaJual', models.DecimalField(blank=True, db_column='HargaJual', decimal_places=4, max_digits=12, null=True)),
                ('StokIDR', models.DecimalField(blank=True, db_column='StokIDR', decimal_places=4, max_digits=12, null=True)),
                ('KategoriBahan', models.CharField(blank=True, db_column='KategoriBahan', max_length=10, null=True)),
                ('Keterangan', models.TextField(blank=True, db_column='Keterangan', null=True)),
                ('StokMinimum', models.IntegerField(blank=True, db_column='StokMinimum', null=True)),
                ('Aktif', models.BooleanField(blank=True, db_column='Aktif', default=True, null=True)),
                ('Departemen', models.CharField(blank=True, db_column='Departemen', max_length=20, null=True)),
                ('Supplier', models.TextField(blank=True, db_column='Supplier', null=True)),
                ('NoReg', models.CharField(blank=True, db_column='NoReg', max_length=50, null=True)),
                ('BahanAktif', models.CharField(blank=True, db_column='BahanAktif', max_length=50, null=True)),
                ('Golongan', models.CharField(blank=True, db_column='Golongan', max_length=50, null=True)),
                ('Manufacturer', models.CharField(blank=True, db_column='Manufacturer', max_length=50, null=True)),
                ('Konsentrasi', models.CharField(blank=True, db_column='Konsentrasi', max_length=50, null=True)),
                ('Dosis', models.CharField(blank=True, db_column='Dosis', max_length=50, null=True)),
                ('HamaSasaran', models.CharField(blank=True, db_column='HamaSasaran', max_length=50, null=True)),
                ('TahunSKMentan', models.DateTimeField(blank=True, db_column='TahunSKMentan', null=True)),
                ('TglKadaluarsaKompes', models.DateTimeField(blank=True, db_column='TglKadaluarsaKompes', null=True)),
                ('TglSDS', models.DateTimeField(blank=True, db_column='TglSDS', null=True)),
                ('TambahBahan', models.BooleanField(blank=True, db_column='TambahBahan', default=True, null=True)),
            ],
            options={
                'db_table': 'Bahan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kontrak',
            fields=[
                ('Kode', models.CharField(db_column='Kode', max_length=10, primary_key=True, serialize=False)),
                ('Grup', models.CharField(blank=True, db_column='Grup', max_length=10, null=True)),
                ('FrekuensiKunjungan', models.IntegerField(blank=True, db_column='FrekuensiKunjungan', null=True)),
                ('TglMulai', models.DateTimeField(blank=True, db_column='TglMulai', null=True)),
                ('TglSelesai', models.DateTimeField(blank=True, db_column='TglSelesai', null=True)),
                ('AreaPekerjaan', models.CharField(blank=True, db_column='AreaPekerjaan', max_length=200, null=True)),
                ('CreateDate', models.DateTimeField(blank=True, db_column='CreateDate', null=True)),
                ('CreateBy', models.CharField(blank=True, db_column='CreateBy', max_length=10, null=True)),
                ('Operator', models.CharField(blank=True, db_column='Operator', max_length=10, null=True)),
                ('TglEntry', models.DateTimeField(blank=True, db_column='TglEntry', null=True)),
                ('TanggalKontrak', models.DateTimeField(blank=True, db_column='TanggalKontrak', null=True)),
                ('Pegawai', models.CharField(blank=True, db_column='Pegawai', max_length=10, null=True)),
                ('InsentifAdmin', models.DecimalField(blank=True, db_column='InsentifAdmin', decimal_places=4, max_digits=12, null=True)),
                ('Teknisi', models.CharField(blank=True, db_column='Teknisi', max_length=10, null=True)),
                ('InsentifTeknisi', models.DecimalField(blank=True, db_column='InsentifTeknisi', decimal_places=4, max_digits=12, null=True)),
                ('InsentifSales', models.DecimalField(blank=True, db_column='InsentifSales', decimal_places=4, max_digits=12, null=True)),
                ('JumlahDokumen', models.IntegerField(blank=True, db_column='JumlahDokumen', null=True)),
                ('Harga', models.DecimalField(blank=True, db_column='Harga', decimal_places=4, max_digits=12, null=True)),
                ('JangkaWaktuPerjanjian', models.CharField(blank=True, db_column='JangkaWaktuPerjanjian', max_length=50, null=True)),
                ('CaraPembayaran', models.CharField(blank=True, db_column='CaraPembayaran', max_length=30, null=True)),
                ('Status', models.CharField(blank=True, db_column='Status', max_length=50, null=True)),
                ('Keterangan', models.TextField(blank=True, db_column='Keterangan', null=True)),
                ('NoOrder', models.CharField(blank=True, db_column='NoOrder', max_length=50, null=True)),
                ('NoKontrak', models.CharField(blank=True, db_column='NoKontrak', max_length=50, null=True)),
                ('TipePekerjaan', models.CharField(blank=True, db_column='TipePekerjaan', max_length=50, null=True)),
                ('Departemen', models.CharField(blank=True, db_column='Departemen', max_length=20, null=True)),
                ('Termin', models.IntegerField(blank=True, db_column='Termin', null=True)),
                ('PlafonOperasional', models.DecimalField(blank=True, db_column='PlafonOperasional', decimal_places=4, max_digits=12, null=True)),
                ('PlafonInsentif', models.DecimalField(blank=True, db_column='PlafonIinsentif', decimal_places=4, max_digits=12, null=True)),
                ('JangkaWaktuPerjanjian2', models.IntegerField(blank=True, db_column='JangkaWaktuPerjanjian2', null=True)),
                ('Verifikasi', models.BooleanField(blank=True, db_column='Verifikasi', default=True, null=True)),
                ('InsentifTambahan', models.DecimalField(blank=True, db_column='InsentifTambahan', decimal_places=4, max_digits=12, null=True)),
                ('Hari', models.IntegerField(blank=True, db_column='Hari', null=True)),
                ('Putus', models.BooleanField(blank=True, db_column='Putus', default=True, null=True)),
                ('Tipe', models.CharField(blank=True, db_column='Tipe', max_length=50, null=True)),
                ('JenisLaporan', models.CharField(blank=True, db_column='JenisLaporan', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Kontrak',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('Kode', models.CharField(db_column='Kode', max_length=10, primary_key=True, serialize=False)),
                ('Nama', models.CharField(blank=True, db_column='Nama', max_length=250, null=True)),
                ('Alamat', models.CharField(blank=True, db_column='Alamat', max_length=250, null=True)),
                ('BidangUsaha', models.CharField(blank=True, db_column='BidangUsaha', max_length=50, null=True)),
                ('Tgl', models.DateTimeField(blank=True, db_column='Tgl', null=True)),
                ('Telp', models.CharField(blank=True, db_column='Telp', max_length=20, null=True)),
                ('Fax', models.CharField(blank=True, db_column='Fax', max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, db_column='Email', default='name@gmail.com', max_length=50, null=True)),
                ('NPWP', models.BooleanField(blank=True, db_column='NPWP', default=True, null=True)),
                ('NoNPWP', models.CharField(blank=True, db_column='NoNPWP', max_length=100, null=True)),
                ('AlamatNPWP', models.CharField(blank=True, db_column='AlamatNPWP', max_length=100, null=True)),
                ('PIC1Nama', models.CharField(blank=True, db_column='PIC1Nama', max_length=100, null=True)),
                ('PIC1Jabatan', models.CharField(blank=True, db_column='PIC1Jabatan', max_length=50, null=True)),
                ('PIC1Telp', models.CharField(blank=True, db_column='PIC1Telp', max_length=20, null=True)),
                ('PIC2Nama', models.CharField(blank=True, db_column='PIC2Nama', max_length=100, null=True)),
                ('PIC2Jabatan', models.CharField(blank=True, db_column='PIC2Jabatan', max_length=50, null=True)),
                ('PIC2Telp', models.CharField(blank=True, db_column='PIC2Telp', max_length=20, null=True)),
                ('PIC3Nama', models.CharField(blank=True, db_column='PIC3Nama', max_length=100, null=True)),
                ('PIC3Jabatan', models.CharField(blank=True, db_column='PIC3Jabatan', max_length=50, null=True)),
                ('PIC3Telp', models.CharField(blank=True, db_column='PIC3Telp', max_length=20, null=True)),
                ('JenisUsaha', models.CharField(blank=True, db_column='JenisUsaha', max_length=10, null=True)),
                ('PPN', models.BooleanField(blank=True, db_column='PPN', default=True, null=True)),
                ('Aktif', models.BooleanField(blank=True, db_column='Aktif', default=True, null=True)),
                ('Prc', models.BooleanField(blank=True, db_column='Prc', default=True, null=True)),
                ('Tc', models.BooleanField(blank=True, db_column='Tc', default=True, null=True)),
                ('Fumigrasi', models.BooleanField(blank=True, db_column='Fumigrasi', default=True, null=True)),
                ('Trading', models.BooleanField(blank=True, db_column='Trading', default=True, null=True)),
                ('Keterangan', models.TextField(blank=True, db_column='Keterangan', null=True)),
                ('CPPro', models.BooleanField(blank=True, db_column='CPPro', default=True, null=True)),
                ('Termin', models.IntegerField(blank=True, db_column='Termin', null=True)),
                ('CreateBy', models.CharField(blank=True, db_column='CreateBy', max_length=20, null=True)),
                ('CreateDate', models.DateTimeField(blank=True, db_column='CreateDate', null=True)),
                ('Operator', models.CharField(blank=True, db_column='Operator', max_length=20, null=True)),
                ('TglEntry', models.DateTimeField(blank=True, db_column='TglEntry', null=True)),
            ],
            options={
                'db_table': 'Pelanggan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Penawaran',
            fields=[
                ('Kode', models.CharField(db_column='Kode', max_length=10, primary_key=True, serialize=False)),
                ('Tanggal', models.DateTimeField(blank=True, db_column='Tanggal', null=True)),
                ('AlamatTreatment', models.CharField(blank=True, db_column='AlamatTreatment', max_length=250, null=True)),
                ('JenisPekerjaan', models.CharField(blank=True, db_column='JenisPekerjaan', max_length=50, null=True)),
                ('Metode', models.CharField(blank=True, db_column='Metode', max_length=50, null=True)),
                ('Harga', models.DecimalField(blank=True, db_column='Harga', decimal_places=4, max_digits=12, null=True)),
                ('Keterangan', models.TextField(blank=True, db_column='Keterangan', null=True)),
                ('CreateDate', models.DateTimeField(blank=True, db_column='CreateDate', null=True)),
                ('CreateBy', models.CharField(blank=True, db_column='CreateBy', max_length=50, null=True)),
                ('Operator', models.CharField(blank=True, db_column='Operator', max_length=50, null=True)),
                ('TglEntry', models.DateTimeField(blank=True, db_column='TglEntry', null=True)),
                ('Sales', models.CharField(blank=True, db_column='Sales', max_length=10, null=True)),
                ('TanggalPeriode', models.DateTimeField(blank=True, db_column='TanggalPeriode', null=True)),
                ('Status', models.CharField(blank=True, db_column='Status', max_length=20, null=True)),
                ('NoPenawaran', models.CharField(blank=True, db_column='NoPenawaran', max_length=50, null=True)),
                ('HargaDeal', models.DecimalField(blank=True, db_column='HargaDeal', decimal_places=4, max_digits=12, null=True)),
                ('TglDeal', models.DateTimeField(blank=True, db_column='TglDeal', null=True)),
                ('Sumber', models.CharField(blank=True, db_column='Sumber', max_length=50, null=True)),
                ('ReferralLead', models.CharField(blank=True, db_column='ReferralLead', max_length=250, null=True)),
            ],
            options={
                'db_table': 'Penawaran',
                'managed': False,
            },
        ),
    ]
