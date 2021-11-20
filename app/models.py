"""
Definition of models.
"""

from django.db import models
from django.urls import reverse

# Create your models here.

class Pelanggan(models.Model):
    Kode = models.CharField(max_length=10, db_column="Kode", primary_key=True)
    Nama = models.CharField(max_length=250, blank=True, null=True, db_column="Nama")
    Alamat = models.CharField(max_length=250, db_column="Alamat", blank=True, null=True)
    BidangUsaha = models.CharField(max_length=50, db_column="BidangUsaha", blank=True, null=True)
    Tgl = models.DateTimeField(null=True, blank=True, db_column="Tgl")
    Telp = models.CharField(max_length=20, null=True, db_column="Telp", blank=True)
    Fax = models.CharField(max_length=50, null=True, db_column="Fax", blank=True)
    Email = models.EmailField(max_length=50, default='name@gmail.com', db_column="Email", blank=True, null=True)
    NPWP = models.BooleanField(default=True, db_column="NPWP", blank=True, null=True)
    NoNPWP = models.CharField(max_length=100, null=True, db_column="NoNPWP", blank=True)
    AlamatNPWP = models.CharField(max_length=100, null=True, db_column="AlamatNPWP", blank=True)
    PIC1Nama = models.CharField(max_length=100, null=True, db_column="PIC1Nama", blank=True)   
    PIC1Jabatan = models.CharField(max_length=50, null=True, db_column="PIC1Jabatan", blank=True)
    PIC1Telp = models.CharField(max_length=20, null=True, db_column="PIC1Telp", blank=True)
    PIC2Nama = models.CharField(max_length=100, null=True, db_column="PIC2Nama", blank=True)
    PIC2Jabatan = models.CharField(max_length=50, null=True, db_column="PIC2Jabatan", blank=True)
    PIC2Telp = models.CharField(max_length=20, null=True, db_column="PIC2Telp", blank=True)
    PIC3Nama = models.CharField(max_length=100, null=True, db_column="PIC3Nama", blank=True)
    PIC3Jabatan = models.CharField(max_length=50, null=True, db_column="PIC3Jabatan", blank=True)
    PIC3Telp = models.CharField(max_length=20, null=True, db_column="PIC3Telp", blank=True)
    JenisUsaha = models.CharField(max_length=10, null=True, db_column="JenisUsaha", blank=True)
    PPN = models.BooleanField(default=True, db_column="PPN", blank=True, null=True)
    Aktif = models.BooleanField(default=True, db_column="Aktif", blank=True, null=True)
    Prc = models.BooleanField(default=True, db_column="Prc", blank=True, null=True)
    Tc = models.BooleanField(default=True, db_column="Tc", blank=True, null=True)
    Fumigrasi = models.BooleanField(default=True, db_column="Fumigrasi", blank=True, null=True)
    Trading = models.BooleanField(default=True, db_column="Trading", blank=True, null=True)
    Keterangan = models.TextField(null=True, db_column="Keterangan", blank=True)
    CPPro = models.BooleanField(default=True, db_column="CPPro", blank=True, null=True)
    Termin = models.IntegerField(null=True, db_column="Termin", blank=True)
    CreateBy = models.CharField(max_length=20, null=True, blank=True, db_column="CreateBy")
    CreateDate = models.DateTimeField(null=True, blank=True, db_column="CreateDate")
    Operator = models.CharField(max_length=20, null=True, db_column="Operator", blank=True)
    TglEntry = models.DateTimeField(null=True, blank=True, db_column="TglEntry")

    def jumlah_kontrak(self):
        return self.kontrak_set.count()

    def __str__(self):
        if self.Nama is not None:
            return self.Nama
        else:
            return ""
    
    class Meta:
        db_table = "Pelanggan"
        managed = False
        verbose_name_plural = "Pelanggan"

class Penawaran(models.Model):
    Kode = models.CharField(max_length=10, primary_key=True, db_column="Kode")
    Tanggal = models.DateTimeField(null=True, blank=True, db_column="Tanggal")
    pelanggan = models.ForeignKey(Pelanggan, db_column="Pelanggan", on_delete=models.SET_NULL, null=True, blank=True)
    AlamatTreatment = models.CharField(max_length=250, null=True, blank=True, db_column="AlamatTreatment")
    JenisPekerjaan = models.CharField(max_length=50, null=True, blank=True, db_column="JenisPekerjaan")
    Metode = models.CharField(max_length=50, null=True, blank=True, db_column="Metode")
    Harga = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True, db_column="Harga")
    Keterangan = models.TextField(null=True, blank=True, db_column="Keterangan")
    CreateDate = models.DateTimeField(null=True, blank=True, db_column="CreateDate")
    CreateBy = models.CharField(max_length=50, null=True, blank=True, db_column="CreateBy")
    Operator = models.CharField(max_length=50, null=True, blank=True, db_column="Operator")
    TglEntry = models.DateTimeField(null=True, blank=True, db_column="TglEntry")
    Sales = models.ForeignKey("Pegawai", db_column="Sales", on_delete=models.SET_NULL, null=True, blank=True)
    TanggalPeriode = models.DateTimeField(null=True, blank=True, db_column="TanggalPeriode")
    Status = models.CharField(max_length=20, null=True, blank=True, db_column="Status")
    NoPenawaran = models.CharField(max_length=50, null=True, blank=True, db_column="NoPenawaran")
    HargaDeal = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True, db_column="HargaDeal")
    TglDeal = models.DateTimeField(null=True, blank=True, db_column="TglDeal")
    Sumber = models.CharField(max_length=50, null=True, blank=True, db_column="Sumber")
    ReferralLead = models.CharField(max_length=250, null=True, blank=True, db_column="ReferralLead")

    def __str__(self):
        if self.pelanggan is not None:
            return (self.Kode + " / " + self.pelanggan.Nama)
        else:
            return ""

    class Meta:
        db_table = "Penawaran"
        managed = False
        verbose_name_plural = "Penawaran"

    def get_absolute_url(self):
        return reverse('penawaran_list')

class Kontrak(models.Model):
    Kode = models.CharField(max_length=10, primary_key=True, db_column="Kode", default="New")
    penawaran = models.ForeignKey('Penawaran', db_column="Penawaran", on_delete=models.SET_NULL, null=True, blank=True)
    JobLama = models.ForeignKey('self', on_delete=models.SET_NULL, db_column="JobLama", null=True, blank=True)
    Grup = models.CharField(max_length=10, db_column="Grup", null=True, blank=True)
    pelanggan = models.ForeignKey(Pelanggan, db_column="Pelanggan", on_delete=models.SET_NULL, null=True, blank=True)
    FrekuensiKunjungan = models.IntegerField(db_column="FrekuensiKunjungan", null=True, blank=True)
    TglMulai = models.DateTimeField(null=True, blank=True, db_column="TglMulai")
    TglSelesai = models.DateTimeField(null=True, blank=True, db_column="TglSelesai")
    AreaPekerjaan = models.CharField(max_length=200, db_column="AreaPekerjaan", null=True, blank=True)
    CreateDate = models.DateTimeField(null=True, blank=True, db_column="CreateDate")
    CreateBy = models.CharField(max_length=10, null=True, blank=True, db_column="CreateBy")
    Operator = models.CharField(max_length=10, null=True, blank=True, db_column="Operator")
    TglEntry = models.DateTimeField(null=True, blank=True, db_column="TglEntry")
    TanggalKontrak = models.DateTimeField(null=True, blank=True, db_column="TanggalKontrak")
    Pegawai = models.ForeignKey("Pegawai", db_column="Pegawai", on_delete=models.SET_NULL, null=True, blank=True, related_name="Pegawai")
    InsentifAdmin = models.DecimalField(max_digits=12, decimal_places=4, db_column="InsentifAdmin", null=True, blank=True)
    Teknisi = models.ForeignKey("Pegawai", db_column="Teknisi", on_delete=models.SET_NULL, null=True, blank=True, related_name="Teknisi")
    InsentifTeknisi = models.DecimalField(max_digits=12, decimal_places=4, db_column="InsentifTeknisi", null=True, blank=True)
    InsentifSales = models.DecimalField(max_digits=12, decimal_places=4, db_column="InsentifSales", null=True, blank=True)
    JumlahDokumen = models.IntegerField(null=True, blank=True, db_column="JumlahDokumen")
    Harga = models.DecimalField(max_digits=12, decimal_places=4, db_column="Harga", null=True, blank=True)
    JangkaWaktuPerjanjian = models.CharField(max_length=50, null=True, blank=True, db_column="JangkaWaktuPerjanjian")
    CaraPembayaran = models.CharField(max_length=30, null=True, blank=True, db_column="CaraPembayaran")
    Status = models.CharField(max_length=50, null=True, blank=True, db_column="Status")
    Keterangan = models.TextField(null=True, blank=True, db_column="Keterangan")
    NoOrder = models.CharField(max_length=50, null=True, blank=True, db_column="NoOrder")
    NoKontrak = models.CharField(max_length=50, null=True, blank=True, db_column="NoKontrak")
    TipePekerjaan = models.CharField(max_length=50, null=True, blank=True, db_column="TipePekerjaan")
    Departemen = models.CharField(max_length=20, null=True, blank=True, db_column="Departemen")
    Termin = models.IntegerField(null=True, blank=True, db_column="Termin")
    PlafonOperasional = models.DecimalField(max_digits=12, decimal_places=4, db_column="PlafonOperasional", null=True, blank=True)
    PlafonInsentif = models.DecimalField(max_digits=12, decimal_places=4, db_column="PlafonIinsentif", null=True, blank=True)
    JangkaWaktuPerjanjian2 = models.IntegerField(null=True, blank=True, db_column="JangkaWaktuPerjanjian2")
    Verifikasi = models.BooleanField(default=True, db_column="Verifikasi", blank=True, null=True)
    InsentifTambahan = models.DecimalField(max_digits=12, decimal_places=4, db_column="InsentifTambahan", null=True, blank=True)
    Hari = models.IntegerField(null=True, blank=True, db_column="Hari")
    Putus = models.BooleanField(default=True, db_column="Putus", blank=True, null=True)
    Tipe = models.CharField(max_length=50, null=True, blank=True, db_column="Tipe")
    JenisLaporan = models.CharField(max_length=50, null=True, blank=True, db_column="JenisLaporan")


    def __str__(self):
        if self.Kode is not None:
            return self.Kode
        else:
            return ""

    class Meta:
        db_table = "Kontrak"
        managed = False
        verbose_name_plural = "Kontrak"

# db_column, db_table
# primary_key
# tipe data hrs benar, max_Length sesuai
# null true, blank true

class Bahan(models.Model):
    Kode = models.CharField(max_length=20, db_column="Kode", primary_key=True)
    Nama = models.CharField(max_length=250, db_column="Nama", null=True, blank=True)
    Tipe = models.CharField(max_length=50, db_column="Tipe", null=True, blank=True)
    Qty = models.IntegerField(null=True, db_column="Qty", blank=True)
    Satuan = models.CharField(max_length=10, db_column="Satuan", null=True, blank=True)
    HargaBeli = models.DecimalField(max_digits=12, decimal_places=4, db_column="HargaBeli", null=True, blank=True)
    HargaJual =  models.DecimalField(max_digits=12, decimal_places=4, db_column="HargaJual", null=True, blank=True)
    StokIDR =  models.DecimalField(max_digits=12, decimal_places=4, db_column="StokIDR", null=True, blank=True)
    KategoriBahan = models.CharField(max_length=10, db_column="KategoriBahan", null=True, blank=True)
    Keterangan = models.TextField(db_column="Keterangan", null=True, blank=True)
    StokMinimum = models.IntegerField(null=True, db_column="StokMinimum", blank=True)
    Aktif = models.BooleanField(default=True, db_column="Aktif", blank=True, null=True)
    Departemen = models.CharField(max_length=20, db_column="Departemen", null=True, blank=True)
    Supplier = models.TextField(db_column="Supplier", null=True, blank=True)
    NoReg = models.CharField(max_length=50, db_column="NoReg", null=True, blank=True)
    BahanAktif = models.CharField(max_length=50, db_column="BahanAktif", null=True, blank=True)
    Golongan = models.CharField(max_length=50, db_column="Golongan", null=True, blank=True)
    Manufacturer = models.CharField(max_length=50, db_column="Manufacturer", null=True, blank=True)
    Konsentrasi = models.CharField(max_length=50, db_column="Konsentrasi", null=True, blank=True)
    Dosis = models.CharField(max_length=50, db_column="Dosis", null=True, blank=True)
    HamaSasaran = models.CharField(max_length=50, db_column="HamaSasaran", null=True, blank=True)
    TahunSKMentan = models.DateTimeField(db_column="TahunSKMentan", null=True, blank=True)
    TglKadaluarsaKompes = models.DateTimeField(db_column="TglKadaluarsaKompes", null=True, blank=True)
    TglSDS = models.DateTimeField(db_column="TglSDS", null=True, blank=True)
    TambahBahan = models.BooleanField(default=True, db_column="TambahBahan", null=True, blank=True)

    def __str__(self):
        if self.Nama is not None:
            return self.Nama
        else:
            return ""

    class Meta:
        db_table = "Bahan"
        managed = False
        verbose_name_plural = "Bahan"

class DetailKontrakBahan(models.Model):
    kode = models.IntegerField(primary_key=True, db_column="kode")
    kontrak = models.ForeignKey(Kontrak, on_delete=models.SET_NULL, db_column="kontrak", null=True, blank=True)
    bahan = models.ForeignKey(Bahan, on_delete=models.SET_NULL, db_column="bahan", null=True, blank=True)
    KategoriBahan = models.CharField(max_length=10, null=True, blank=True, db_column="KategoriBahan")
    Qty = models.IntegerField(null=True, blank=True, db_column="Qty")

    class Meta:
        db_table = "DetailKontrakBahan"
        managed = False

class DetailKontrakPerlengkapan(models.Model):
    kode = models.IntegerField(primary_key=True, db_column="kode")
    kontrak = models.ForeignKey(Kontrak, on_delete=models.SET_NULL, db_column="kontrak", null=True, blank=True)
    Perlengkapan = models.CharField(max_length=10, null=True, blank=True, db_column="Perlengkapan")
    Nominal = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True, db_column="Nominal")
    Qty = models.IntegerField(null=True, blank=True, db_column="Qty")

    class Meta:
        db_table = "DetailKontrakPerlengkapan"
        managed = False

class STSPR(models.Model):
    Kode = models.CharField(max_length=10, primary_key=True, db_column="Kode", default="New")
    JobOrder = models.CharField(max_length=10, null=True, blank=True, db_column="JobOrder")
    KetJasTre = models.TextField(null=True, blank=True, db_column="KetJasTre")
    NoInvoice = models.CharField(max_length=50, null=True, blank=True, db_column="NoInvoice")
    NoRekening = models.CharField(max_length=200, null=True, blank=True, db_column="NoRekening")
    Tanggal = models.DateTimeField(db_column="Tanggal", null=True, blank=True)
    WaktuMulai = models.DateTimeField(db_column="WaktuMulai", null=True, blank=True)
    WaktuSelesai = models.DateTimeField(db_column="WaktuSelesai", null=True, blank=True)
    Teknisi = models.CharField(max_length=10, null=True, blank=True, db_column="Teknisi")
    JenisPekerjaan = models.CharField(max_length=200, null=True, blank=True, db_column="JenisPekerjaan")
    Jumlah = models.IntegerField(null=True, blank=True, db_column="Jumlah")
    GrandTotal = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True, db_column="GrandTotal")
    Harga = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True, db_column="Harga")
    PPN1 = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True, db_column="PPN1")
    Tindakan = models.TextField(null=True, blank=True, db_column="Tindakan")
    CreateBy = models.CharField(max_length=10, null=True, blank=True, db_column="CreateBy")
    CreateDate = models.DateTimeField(null=True, blank=True, db_column="CreateDate")
    Operator = models.CharField(max_length=10, null=True, blank=True, db_column="Operator")
    TglEntry = models.DateTimeField(db_column="TglEntry", null=True, blank=True)
    PPN = models.BooleanField(default=True, db_column="PPN", blank=True, null=True)
    TidakInvoice = models.BooleanField(default=True, db_column="TidakInvoice", blank=True, null=True)
    NoFakturPajak = models.CharField(max_length=50, null=True, blank=True, db_column="NoFakturPajak")
    Grup = models.CharField(max_length=10, null=True, blank=True, db_column="Grup")
    TglTerimaInvoice = models.DateTimeField(db_column="TglTerimaInvoice", null=True, blank=True)
    Tanggal2 = models.DateTimeField(db_column="Tanggal2", null=True, blank=True)
    STS = models.CharField(max_length=10, null=True, blank=True, db_column="STS")
    Memo = models.TextField(null=True, blank=True, db_column="Memo")
    TglSelesaiLaporan = models.DateTimeField(db_column="TglSelesaiLaporan", null=True, blank=True)
    Status1 = models.CharField(max_length=20, null=True, blank=True, db_column="Status1")
    Alasan = models.TextField(null=True, blank=True, db_column="Alasan")
    NoOrder = models.CharField(max_length=50, null=True, blank=True, db_column="NoOrder")

    class Meta:
        db_table = "STSPR"
        managed = False
        verbose_name_plural = "STSPR"

    def __str__(self):
        if self.Kode is not None:
            return self.Kode
        else:
            return ""

class DetailSTSPR(models.Model):
    Kode =  models.IntegerField(primary_key=True, db_column="Kode")
    sTSPR = models.ForeignKey(STSPR, on_delete=models.SET_NULL, db_column="STSPR", null=True, blank=True)
    bahan = models.ForeignKey(Bahan, on_delete=models.SET_NULL, db_column="Bahan", null=True, blank=True)
    Qty = models.IntegerField(null=True, blank=True, db_column="Qty")
    PlafonQty = models.IntegerField(null=True, blank=True, db_column="PlafonQty")
    Invoice = models.CharField(max_length=10, null=True, blank=True, db_column="Invoice")

    class Meta:     
        db_table = "DetailSTSPR"
        managed = False

class DetailSTSPRHarian(models.Model):
    STSPRH = models.CharField(primary_key=True, max_length=10, db_column="STSPRH")
    sTSPR = models.ForeignKey(STSPR, on_delete=models.SET_NULL, db_column="STSPR", null=True, blank=True)
    Tanggal = models.DateTimeField(null=True, blank=True, db_column="Tanggal")
    Komplain = models.BooleanField(default=True, db_column="Komplain", blank=True, null=True)
    Keterangan = models.TextField(null=True, blank=True, db_column="Keterangan")
    JamMulai = models.DateTimeField(null=True, blank=True, db_column="JamMulai")
    JamSelesai = models.DateTimeField(null=True, blank=True, db_column="JamSelesai")
    JenisPekerjaan = models.CharField(max_length=50, null=True, blank=True, db_column="JenisPekerjaan")
    Inpeksi = models.CharField(max_length=250, null=True, blank=True, db_column="Inpeksi")
    Spraying = models.CharField(max_length=250, null=True, blank=True, db_column="Spraying")
    CoolFogging = models.CharField(max_length=250, null=True, blank=True, db_column="CoolFogging")
    ThermalFogging = models.CharField(max_length=250, null=True, blank=True, db_column="ThermalFogging")
    Inpeksi1 = models.BooleanField(default=True, db_column="Inpeksi1", blank=True, null=True)
    Spraying1 = models.BooleanField(default=True, db_column="Spraying1", blank=True, null=True)
    CoolFogging1 = models.BooleanField(default=True, db_column="CoolFogging1", blank=True, null=True)
    ThermalFogging1 = models.BooleanField(default=True, db_column="ThermalFogging1", blank=True, null=True)
    PICClient = models.CharField(max_length=250, null=True, blank=True, db_column="PICClient")
    PICClient1 = models.BooleanField(default=True, db_column="PICClient1", blank=True, null=True)

    class Meta:
        db_table = "DetailSTSPRHarian"
        managed = False

class DetailSTSPRHarianBahan(models.Model):
    Kode = models.IntegerField(primary_key=True, db_column="Kode")
    sTSPR = models.ForeignKey(STSPR, on_delete=models.SET_NULL, db_column="STSPR", null=True, blank=True)
    STSPRH = STSPRH = models.CharField(max_length=10, null=True, blank=True, db_column="STSPRH")
    bahan = models.ForeignKey(Bahan, on_delete=models.SET_NULL, db_column="Bahan", null=True, blank=True)
    Teknisi = models.CharField(max_length=10, null=True, blank=True, db_column="Teknisi")
    Satuan = models.CharField(max_length=50, null=True, blank=True, db_column="Satuan")
    Qty = models.IntegerField(null=True, blank=True, db_column="Qty")

    class Meta:
        db_table = "DetailSTSPRHarianBahan"
        managed = False

class DetailSTSPRHarianTeknisi(models.Model):
    Kode = models.IntegerField(primary_key=True, db_column="Kode")
    sTSPR = models.ForeignKey(STSPR, on_delete=models.SET_NULL, db_column="STSPR", null=True, blank=True)
    STSPRH = models.CharField(max_length=10, null=True, blank=True, db_column="STSPRH")
    Teknisi = models.CharField(max_length=10, null=True, blank=True, db_column="Teknisi")
    JobOrder = models.CharField(max_length=10, null=True, blank=True, db_column="JobOrder")

    class Meta:
        db_table = "DetailSTSPRHarianTeknisi"
        managed = False

class DetailSTSPRPIn(models.Model):
    Kode = models.IntegerField(primary_key=True, db_column="Kode")
    sTSPR = models.ForeignKey(STSPR, on_delete=models.SET_NULL, db_column="STSPR", null=True, blank=True)
    Perlengkapan = models.CharField(max_length=10, null=True, blank=True, db_column="Perlengkapan")
    Tanggal = models.DateTimeField(null=True, blank=True, db_column="Tanggal")

    class Meta:
        db_table = "DetailSTSPRPIn"
        managed = False

class DetailSTSPRPOut(models.Model):
    Kode = models.IntegerField(primary_key=True, db_column="Kode")
    sTSPR = models.ForeignKey(STSPR, on_delete=models.SET_NULL, db_column="STSPR", null=True, blank=True)
    Perlengkapan = models.CharField(max_length=10, null=True, blank=True, db_column="Perlengkapan")
    Tanggal = models.DateTimeField(null=True, blank=True, db_column="Tanggal")

    class Meta:
        db_table = "DetailSTSPRPOut"
        managed = False

class Pegawai(models.Model):
    Kode = models.CharField(max_length=10, primary_key=True, db_column="Kode")
    Nama = models.CharField(max_length=250, null=True, blank=True, db_column="Nama")
    NIK = models.CharField(max_length=50, null=True, blank=True, db_column="NIK")
    NoKTP = models.CharField(max_length=50, null=True, blank=True, db_column="NoKTP")
    NoSIM = models.CharField(max_length=50, null=True, blank=True, db_column="NoSIM")
    Alamat = models.CharField(max_length=250, null=True, blank=True, db_column="Alamat")
    TglLahir = models.DateTimeField(null=True, blank=True, db_column="TglLahir")
    StatusPerkawinan = models.CharField(max_length=20, null=True, blank=True, db_column="StatusPerkawinan")
    Telp = models.CharField(max_length=20, null=True, blank=True, db_column="Telp")
    Hp1 = models.CharField(max_length=15, null=True, blank=True, db_column="Hp1")
    Hp2 = models.CharField(max_length=15, null=True, blank=True, db_column="Hp2")
    TglBergabung = models.DateTimeField(null=True, blank=True, db_column="TglBergabung")
    TglKeluar =  models.DateTimeField(null=True, blank=True, db_column="TglKeluar")
    Keterangan = models.CharField(max_length=50, null=True, blank=True, db_column="Keterangan")
    Bagian = models.CharField(max_length=50, null=True, blank=True, db_column="Bagian")
    Jabatan = models.CharField(max_length=50, null=True, blank=True, db_column="Jabatan")
    Pendidikan = models.CharField(max_length=50, null=True, blank=True, db_column="Pendidikan")
    NoRekening = models.CharField(max_length=50, null=True, blank=True, db_column="NoRekening")
    Bank = models.CharField(max_length=100, null=True, blank=True, db_column="Bank")
    PlafonService = models.DecimalField(max_digits=12, decimal_places=4, db_column="PlafonService", null=True, blank=True)
    Gaji = models.DecimalField(max_digits=12, decimal_places=4, db_column="Gaji", null=True, blank=True)
    TunjanganJabatan = models.DecimalField(max_digits=12, decimal_places=4, db_column="TunjanganJabatan", null=True, blank=True)
    UangMuka = models.DecimalField(max_digits=12, decimal_places=4, db_column="UangMuka", null=True, blank=True)
    Transport = models.DecimalField(max_digits=12, decimal_places=4, db_column="Transport", null=True, blank=True)
    Pulsa = models.DecimalField(max_digits=12, decimal_places=4, db_column="Pulsa", null=True, blank=True)
    Aktif = models.BooleanField(default=True, db_column="Aktif", blank=True, null=True)
    BPJS =  models.DecimalField(max_digits=12, decimal_places=4, db_column="BPJS", null=True, blank=True)
    BPJSKetenagaKerjaan =  models.DecimalField(max_digits=12, decimal_places=4, db_column="BPJSKetenagaKerjaan", null=True, blank=True)
    NPWP = models.CharField(max_length=50, null=True, blank=True, db_column="NPWP")
    JumlahAnak = models.IntegerField(null=True, db_column="JumlahAnak", blank=True)
    NoKK = models.CharField(max_length=50, null=True, blank=True, db_column="NoKK")
    NamaIstri = models.CharField(max_length=50, null=True, blank=True, db_column="NamaIstri")
    SkillAllowance = models.DecimalField(max_digits=12, decimal_places=4, db_column="SkillAllowance", null=True, blank=True)
    FumigatorAllowance = models.DecimalField(max_digits=12, decimal_places=4, db_column="FumigatorAllowance", null=True, blank=True)
    PositionAllowance = models.DecimalField(max_digits=12, decimal_places=4, db_column="PositionAllowance", null=True, blank=True)
    VehicleRentAllowance = models.DecimalField(max_digits=12, decimal_places=4, db_column="VehicleRentAllowance", null=True, blank=True)
    CreateDate = models.DateTimeField(null=True, blank=True, db_column="CreateDate")
    CreateBy = models.CharField(max_length=10, null=True, blank=True, db_column="CreateBy")
    Operator = models.CharField(max_length=10, null=True, blank=True, db_column="Operator")
    TglEntry = models.DateTimeField(null=True, blank=True, db_column="TglEntry")
    Departemen = models.CharField(max_length=250, null=True, blank=True, db_column="Departemen")
    StatusPajak = models.CharField(max_length=50, null=True, blank=True, db_column="StatusPajak")
    IuranJKK = models.DecimalField(max_digits=12, decimal_places=4, db_column="IuranJKK", null=True, blank=True)
    IuranJKM = models.DecimalField(max_digits=12, decimal_places=4, db_column="IuranJKM", null=True, blank=True)
    IuranJHT = models.DecimalField(max_digits=12, decimal_places=4, db_column="IuranJHT", null=True, blank=True)
    IuranJHT2 = models.DecimalField(max_digits=12, decimal_places=4, db_column="IuranJHT2", null=True, blank=True)
    IuranJP = models.DecimalField(max_digits=12, decimal_places=4, db_column="IuranJP", null=True, blank=True)

    class Meta:
        db_table = "Pegawai"
        managed = False

    def __str__(self):
        if self.Nama is not None:
            return self.Nama
        else:
            return ""

