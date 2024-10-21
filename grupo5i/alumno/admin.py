from django.contrib import admin
from.models import Alumno,FRASE
# Register your models here.


class ComentarioIntLine(admin.TabularInline):
    model=FRASE
    extra=1


class AlumnoAdmin(admin.ModelAdmin):
    fields=["aparterno","amaterno","nombre","fecha_nacimento","fecha_ingreso"]
    list_display=["aparterno","amaterno","nombre"]
    inlines=[ComentarioIntLine]




admin.site.register(Alumno,AlumnoAdmin)

@admin.register(FRASE)
class FRASEAdmin(admin.ModelAdmin):
    fields =["comentario","Alumno_fk"]
    list_display=["comentario"]
    

