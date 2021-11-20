from django.contrib import admin
from django import forms
from .models import Pelanggan, Penawaran, Kontrak, Bahan, DetailKontrakBahan, DetailKontrakPerlengkapan, STSPR
from .models import DetailSTSPR, DetailSTSPRHarian, DetailSTSPRHarianBahan, DetailSTSPRHarianTeknisi, DetailSTSPRPIn, DetailSTSPRPOut
class DetailKontrakBahanInline(admin.TabularInline):
    model = DetailKontrakBahan
    extra = 0

class DetailKontrakPerlengkapanInline(admin.TabularInline):
    model = DetailKontrakPerlengkapan
    extra = 0


@admin.register(Pelanggan)
class PelangganAdmin(admin.ModelAdmin):
    list_display = ("Nama", "Alamat", "BidangUsaha", "jumlah_kontrak")

@admin.register(Penawaran)
class PenawaranAdmin(admin.ModelAdmin):
    list_display = ("Kode", "pelanggan", "AlamatTreatment", "JenisPekerjaan", "Harga")

#class PenawaranChoiceField(forms.ModelChoiceField):
    #def label_from_instance(self, obj):
        #return "Output: {}".format(obj.Kode + " " + obj.pelanggan.Nama.filter(pk=1) + " " + str(obj.AlamatTreatment))

class KontrakAdmin(admin.ModelAdmin):
    list_display = ("Kode", "penawaran", "pelanggan", "CreateDate", "TglEntry", "CreateBy", "Operator")
    fields = ["penawaran", "JobLama", "Grup", "pelanggan", "FrekuensiKunjungan", "TglMulai", "TglSelesai", "AreaPekerjaan", "Operator", "TanggalKontrak", "Pegawai", "InsentifAdmin", "Teknisi", "InsentifTeknisi", "InsentifSales", "JumlahDokumen", "Harga", "JangkaWaktuPerjanjian", "CaraPembayaran", "Status", "Keterangan", "NoOrder", "NoKontrak", "TipePekerjaan", "Departemen", "Termin", "PlafonOperasional", "PlafonInsentif", "JangkaWaktuPerjanjian2", "Verifikasi", "InsentifTambahan", "Hari", "Putus", "Tipe", "JenisLaporan"]
    inlines = [DetailKontrakBahanInline, DetailKontrakPerlengkapanInline]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'CreateBy', None) is None:
            obj.CreateBy = request.user.username
            obj.Operator = request.user.username
        elif getattr(obj, 'Operator', None) != request.user.username:
            obj.Operator = request.user.username
        obj.save()

    #def jumlah_teknisi(self, obj):
     #   return obj.set.count();


    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
        #if db_field.name == 'penawaran': 
         #   return PenawaranChoiceField(queryset=Penawaran.objects.all())
        #return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Kontrak, KontrakAdmin)

@admin.register(Bahan)
class BahanAdmin(admin.ModelAdmin):
    list_display = ("Nama", "Tipe", "Qty", "Satuan")

# Detail STSPR
class DetailSTSPRInline(admin.TabularInline):
    model = DetailSTSPR
    extra = 0

class DetailSTSPRHarianInline(admin.TabularInline):
    model = DetailSTSPRHarian
    extra = 0

class DetailSTSPRHarianBahanInline(admin.TabularInline):
    model = DetailSTSPRHarianBahan
    extra = 0

class DetailSTSPRHarianTeknisiInline(admin.TabularInline):
    model = DetailSTSPRHarianTeknisi
    extra = 0

class DetailSTSPRPInInline(admin.TabularInline):
    model = DetailSTSPRPIn
    extra = 0

class DetailSTSPRPOutInline(admin.TabularInline):
    model = DetailSTSPRPOut
    extra = 0

@admin.register(STSPR)
class STSPRAdmin(admin.ModelAdmin):
    list_display = ("Kode", "JobOrder", "CreateDate", "TglEntry", "CreateBy", "Operator")

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'CreateBy', None) is None:
            obj.CreateBy = request.user.username
            obj.Operator = request.user.username
        elif getattr(obj, 'Operator', None) != request.user.username:
            obj.Operator = request.user.username
        obj.save()

    fields = ["JobOrder", "KetJasTre", "NoInvoice", "NoRekening", "Tanggal", "WaktuMulai", "WaktuSelesai", "Teknisi", "JenisPekerjaan", "Jumlah", "GrandTotal", "Harga", "PPN1", "Tindakan", "PPN", "TidakInvoice", "NoFakturPajak", "Grup", "TglTerimaInvoice", "Tanggal2", "STS", "Memo", "TglSelesaiLaporan", "Status1", "Alasan", "NoOrder"]
    inlines = [DetailSTSPRInline, DetailSTSPRHarianInline, DetailSTSPRHarianBahanInline, DetailSTSPRHarianTeknisiInline, DetailSTSPRPInInline, DetailSTSPRPOutInline]
#@admin.register(Penawaran)
#class PenawaranAdmin(admin.ModelAdmin):
#    list_display = ("Tanggal", "pelanggan", "AlamatTreatment", "JenisPekerjaan")

#@admin.register(Kontrak)
#class KontrakAdmin(admin.ModelAdmin):
#    list_display = ("penawaran", "JobLama", "pelanggan", "FrekuensiKunjungan")