from django.contrib import admin, messages
from django.utils.translation import ngettext
from .models import *

# Register your models here.

class LinkView(admin.ModelAdmin):
    list_display = [
        'nama_dosen',
        'nama_mata_kuliah',
        'link',
        'tanggal',
        'mulai_jam',
        'berakhir_jam'
    ]
    ordering = ['mulai_jam']

class PermanentLinkGmeetView(admin.ModelAdmin):
    list_display = [
        'nama_dosen',
        'nama_mata_kuliah',
        'link',
    ]
    ordering = ['nama_mata_kuliah'
]
class FormatNameGmeetView(admin.ModelAdmin):
    list_display = [
        'nama_dosen',
        'nama_mata_kuliah',
        'format_nama'
    ]
    ordering = ['nama_mata_kuliah']

class LinkGclassroomView(admin.ModelAdmin):
    list_display = [
        'nama_dosen',
        'nama_mata_kuliah',
        'link',
    ]
    ordering = ['nama_dosen']

class TugasView(admin.ModelAdmin):
    actions = [
        'mark_sudah_dikerjakan',
        'pindahkan_ke_tugas_mandiri',
        'pindahkan_ke_tugas_kelompok'
    ]

    list_display = [
        'nama_dosen',
        'nama_mata_kuliah',
        'tugas',
        'deadline',
        'status',
        'tipe_tugas'
    ]
    ordering = ['deadline']

    def mark_sudah_dikerjakan(self, request, queryset):
        updated = queryset.update(status='Sudah dikerjakan')
        self.message_user(request, ngettext(
            '%d tugas was successfully marked as Sudah dikerjakan.',
            '%d tugas were successfully marked as Sudah dikerjakan.',
            updated,
        ) % updated, messages.SUCCESS)

    def pindahkan_ke_tugas_mandiri(self, request, queryset):
        updated = queryset.update(tipe_tugas='TUGAS_MANDIRI')
        self.message_user(request, ngettext(
            '%d tugas berhasil dipindahkan ke tugas mandiri',
            '%d tugas berhasil dipindahkan ke tugas mandiri',
            updated,
        ) % updated, messages.SUCCESS)

    def pindahkan_ke_tugas_kelompok(self, request, queryset):
        updated = queryset.update(tipe_tugas='TUGAS_KELOMPOK')
        self.message_user(request, ngettext(
            '%d tugas berhasil dipindahkan ke tugas kelompok',
            '%d tugas berhasil dipindahkan ke tugas kelompok',
            updated,
        ) % updated, messages.SUCCESS)

class MatKulView(admin.ModelAdmin):
    list_display = [
        'hari',
        'mata_kuliah',
        'nama_dosen',
        'jam_ke',
        'jam_waktu_mulai',
        'jam_waktu_berakhir'
    ]
    ordering = ['hari']

admin.site.register(LinkGoogleMeetorZoom, LinkView)
admin.site.register(PermanentLinkGoogleMeetorZoom, PermanentLinkGmeetView)
admin.site.register(FormatOnlineClass, FormatNameGmeetView)
admin.site.register(LinkGoogleClassroom, LinkGclassroomView)
admin.site.register(Tugas, TugasView)
admin.site.register(JadwalMataKuliah, MatKulView)