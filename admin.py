from django.contrib import admin
from django.utils.html import format_html
from app_escolar_api.models import *


@admin.register(Administradores)
class AdministradoresAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "creation", "update")
    search_fields = ("user__username", "user__email", "user__first_name", "user__last_name")

@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "creation", "update")
    search_fields = ("user__username", "user__email", "user__first_name", "user__last_name")

@admin.register(Maestros)
class MaestrosAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "creation", "update")
    search_fields = ("user__username", "user__email", "user__first_name", "user__last_name")

@admin.register(Materias)
class MateriasAdmin(admin.ModelAdmin):
    list_display = ("id", "nrc", "nombre", "seccion", "get_programa_educativo", "get_profesor", "creation")
    search_fields = ("nrc", "nombre", "profesor__user__first_name", "profesor__user__last_name")
    list_filter = ("programa_educativo",)
    
    def get_programa_educativo(self, obj):
        return obj.programa_educativo or "No asignado"
    get_programa_educativo.short_description = 'Programa Educativo'
    
    def get_profesor(self, obj):
        if obj.profesor and obj.profesor.user:
            return f"{obj.profesor.user.first_name} {obj.profesor.user.last_name}"
        return "No asignado"
    get_profesor.short_description = 'Profesor'