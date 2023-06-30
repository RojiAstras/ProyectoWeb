from django.db import models

class TipoArticulo(models.Model):
    id_tipoArticulo  = models.AutoField(db_column='idTipoArticulo', primary_key=True) 
    tipoArticulo     = models.CharField(max_length=20)

    def __str__(self):
        return str(self.tipoArticulo)

class TipoMascota(models.Model):
    id_tipoMascota  = models.AutoField(db_column='idTipoMascota', primary_key=True) 
    tipoMascota     = models.CharField(max_length=20)

    def __str__(self):
        return str(self.tipoMascota)

# Create your models here.
class Producto(models.Model):
    id_producto         =models.AutoField(db_column='idProducto', primary_key=True)
    nom_producto        =models.CharField(max_length=20)
    img_producto        =models.CharField(max_length=100)
    id_tipoArticulo     = models.ForeignKey('TipoArticulo',on_delete=models.CASCADE, db_column='idTipoArticulo', default=0)
    id_tipoMascota      = models.ForeignKey('TipoMascota',on_delete=models.CASCADE, db_column='idTipoMascota', default=0)    
    detalle_producto    =models.CharField(max_length=50)
    precio_producto     =models.IntegerField()

    def __str__(self):
        return str(self.nom_producto)

class Carrito(models.Model):
    id_producto         =models.AutoField(db_column='idProducto', primary_key=True)
    usuario_var         =models.CharField(max_length=50, default=' ')
    nom_producto        =models.CharField(max_length=20)
    img_producto        =models.CharField(max_length=100)
    precio_producto     =models.IntegerField()

    def __str__(self):
        return str(self.nom_producto)

class Carusel1(models.Model):
    id_carusel        =models.AutoField(db_column='idCarusel1', primary_key=True)
    titulo_car1        =models.CharField(max_length=30)
    img_car1         =models.CharField(max_length=100)
    detalle_car1     =models.CharField(max_length=50)

    def __str__(self):
        return str(self.titulo_car1)

class Carusel2(models.Model):
    id_carusel2        =models.AutoField(db_column='idCarusel2', primary_key=True)
    titulo_car2        =models.CharField(max_length=30)
    img_car2         =models.CharField(max_length=100)
    detalle_car2     =models.CharField(max_length=50)

    def __str__(self):
        return str(self.titulo_car2)

class Banner(models.Model):
    id_Banner       =models.AutoField(db_column='idBanner', primary_key=True)
    img_Banner      =models.CharField(max_length=100)



class Boleta(models.Model):
    id_boleta           =models.AutoField(db_column='idBoleta', primary_key=True)



class DetalleBoleta(models.Model):
    id_detalle          =models.AutoField(db_column='idDetalleBoleta', primary_key=True)
    desc_boleta         =models.CharField(max_length=50)
    id_boleta           = models.ForeignKey('Boleta',on_delete=models.CASCADE, db_column='idBoleta')  

class Empleado(models.Model):
    emp_rut              = models.CharField(primary_key=True, max_length=10)
    emp_nombre           = models.CharField(max_length=20)
    emp_appaterno        = models.CharField(max_length=20)
    emp_apmaterno        = models.CharField(max_length=20)
    emp_fnacimiento      = models.DateField(blank=False, null=False)
    emp_fcontrato        = models.DateField(blank=False, null=False)
    emp_telefono         = models.CharField(max_length=45)
    emp_email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    emp_direccion        = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return str(self.emp_nombre)+" "+str(self.emp_appaterno)   

class Cliente(models.Model):
    cli_rut          = models.CharField(primary_key=True, max_length=10)
    cli_nombre       = models.CharField(max_length=20)
    cli_appaterno    = models.CharField(max_length=20)
    cli_apmaterno    = models.CharField(max_length=20)
    cli_fnacimiento  = models.DateField(blank=False, null=False)
    cli_fcontrato    = models.DateField(blank=False, null=False)
    cli_telefono     = models.CharField(max_length=45)
    cli_email        = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    cli_direccion    = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return str(self.cli_nombre)+" "+str(self.cli_appaterno)   
    
