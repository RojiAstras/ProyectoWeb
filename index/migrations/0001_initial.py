# Generated by Django 4.2.2 on 2023-06-25 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id_Banner', models.AutoField(db_column='idBanner', primary_key=True, serialize=False)),
                ('img_Banner', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(db_column='idBoleta', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_producto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nom_producto', models.CharField(max_length=20)),
                ('img_producto', models.CharField(max_length=100)),
                ('precio_producto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Carusel1',
            fields=[
                ('id_carusel', models.AutoField(db_column='idCarusel1', primary_key=True, serialize=False)),
                ('titulo_car1', models.CharField(max_length=30)),
                ('img_car1', models.CharField(max_length=100)),
                ('detalle_car1', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Carusel2',
            fields=[
                ('id_carusel2', models.AutoField(db_column='idCarusel2', primary_key=True, serialize=False)),
                ('titulo_car2', models.CharField(max_length=30)),
                ('img_car2', models.CharField(max_length=100)),
                ('detalle_car2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cli_nombre', models.CharField(max_length=20)),
                ('cli_appaterno', models.CharField(max_length=20)),
                ('cli_apmaterno', models.CharField(max_length=20)),
                ('cli_fnacimiento', models.DateField()),
                ('cli_fcontrato', models.DateField()),
                ('cli_telefono', models.CharField(max_length=45)),
                ('cli_email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('cli_direccion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('emp_rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('emp_nombre', models.CharField(max_length=20)),
                ('emp_appaterno', models.CharField(max_length=20)),
                ('emp_apmaterno', models.CharField(max_length=20)),
                ('emp_fnacimiento', models.DateField()),
                ('emp_fcontrato', models.DateField()),
                ('emp_telefono', models.CharField(max_length=45)),
                ('emp_email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('emp_direccion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nom_producto', models.CharField(max_length=20)),
                ('img_producto', models.CharField(max_length=100)),
                ('detalle_producto', models.CharField(max_length=50)),
                ('precio_producto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoArticulo',
            fields=[
                ('id_tipoArticulo', models.AutoField(db_column='idTipoArticulo', primary_key=True, serialize=False)),
                ('tipoArticulo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMascota',
            fields=[
                ('id_tipoMascota', models.AutoField(db_column='idTipoMascota', primary_key=True, serialize=False)),
                ('tipoMascota', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id_detalle', models.AutoField(db_column='idDetalleBoleta', primary_key=True, serialize=False)),
                ('desc_boleta', models.CharField(max_length=50)),
                ('id_boleta', models.ForeignKey(db_column='idBoleta', on_delete=django.db.models.deletion.CASCADE, to='index.boleta')),
            ],
        ),
    ]