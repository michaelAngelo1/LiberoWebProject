from django.contrib import admin
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
    list_display = ("Nama", "Alamat", "BidangUsaha")

@admin.register(Penawaran)
class PenawaranAdmin(admin.ModelAdmin):
    list_display = ("Kode", "pelanggan", "AlamatTreatment", "JenisPekerjaan")

@admin.register(Kontrak)
class KontrakAdmin(admin.ModelAdmin):
    list_display = ("Kode", "penawaran", "JobLama", "Grup", "pelanggan")
    inlines = [DetailKontrakBahanInline, DetailKontrakPerlengkapanInline]

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
    list_display = ("Kode", "JobOrder")
    inlines = [DetailSTSPRInline, DetailSTSPRHarianInline, DetailSTSPRHarianBahanInline, DetailSTSPRHarianTeknisiInline, DetailSTSPRPInInline, DetailSTSPRPOutInline]
#@admin.register(Penawaran)
#class PenawaranAdmin(admin.ModelAdmin):
#    list_display = ("Tanggal", "pelanggan", "AlamatTreatment", "JenisPekerjaan")

#@admin.register(Kontrak)
#class KontrakAdmin(admin.ModelAdmin):
#    list_display = ("penawaran", "JobLama", "pelanggan", "FrekuensiKunjungan")