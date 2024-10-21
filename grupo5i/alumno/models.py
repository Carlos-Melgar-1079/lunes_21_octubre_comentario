from django.db import models

# Create your models here.

class Alumno(models.Model):
    aparterno=models.CharField(max_length=50,verbose_name="Apellido Paterno")
    amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno")
    nombre=models.CharField(max_length=100,verbose_name="Nombre (s)")
    fecha_nacimiento=models.DateField(verbose_name="fecha de nacimiento",null=False,blank=False)
    fecha_ingreso=models.DateField(verbose_name="fecha de ingreso",null=False,blank=False)
    
    class Meta:
        db_table="Alumnos"
        verbose_name="Alumno"
        verbose_name_plural="Alumnopapu" #nombre de la tabla
    
    def __str__(self) -> str:
        return self.nombre
    
class FRASE(models.Model):
    comentario=models.TextField(verbose_name="comentario",max_length=400)
    Alumno_fk=models.ForeignKey(Alumno, on_delete=models.CASCADE)

    class Meta:
        verbose_name="FRASE"
        verbose_name_plural="frases"
