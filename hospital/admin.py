from django.contrib import admin
from .models import Patient, Prescription, Drug

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    search_fields = ('name',)

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'context', 'date')
    search_fields = ('patient__name', 'context')
    list_filter = ('date',)

@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count')
    search_fields = ('name',)
