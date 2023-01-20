from django.contrib import admin

# Register your models here.

from . models import DaftarMenu,Karyawan

class TampilMenu(admin.ModelAdmin):
    list_display=('makanan','harga','gambar')
    search_fields=('makanan','harga')

class TampilKaryawan(admin.ModelAdmin):
    list_display=('nama','jabatan','gambar')
    search_fields=('nama','jabatan')
admin.site.register(DaftarMenu,TampilMenu)
admin.site.register(Karyawan,TampilKaryawan)
