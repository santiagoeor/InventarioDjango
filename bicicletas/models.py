from django.db import models

# Create your models here.

class Estado(models.Model):
    propietario = models.CharField(max_length=150, verbose_name="Propietario")
    marca = models.CharField(max_length=150, verbose_name="Marca")
    neomaticos = models.CharField(max_length=150, verbose_name="neomaticos")
    llantas = models.CharField(max_length=150, verbose_name="llantas")
    cadena = models.CharField(max_length=150, verbose_name="cadena")
    plato = models.CharField(max_length=150, verbose_name="plato")
    cassette = models.CharField(max_length=150, verbose_name="cassette")
    sistemafrenos = models.CharField(max_length=150, verbose_name="Sistema de frenos")
    guayascambio = models.CharField(max_length=150, verbose_name="Guayas de Cambio")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        # db_table = ""
        verbose_name = "Estado bicicleta"
        verbose_name_plural = "Estados"

    def __str__(self):
        # self.marca

        return f"{self.propietario}"

class Repuesto(models.Model):
   llantas = models.CharField(max_length=150, verbose_name="llantas") 
   neomaticos = models.CharField(max_length=150, verbose_name="neomaticos") 
   cadenas = models.CharField(max_length=150, verbose_name="cadenas")
   platos = models.CharField(max_length=150, verbose_name="Platos")
   cassettes = models.CharField(max_length=150, verbose_name="Cassettes")
   guayascambio = models.CharField(max_length=150, verbose_name="Guayas de Cambio")
   guayasfrenos = models.CharField(max_length=150, verbose_name="Guayas de frenos")
   create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
   updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

   class Meta:
        # db_table = ""
        verbose_name = "bodega" #interno
        verbose_name_plural = "Repuestos" #externo

