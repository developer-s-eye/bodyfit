# Generated by Django 3.1.6 on 2021-04-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadmililitros', models.IntegerField(db_column='cantidadMililitros')),
            ],
            options={
                'db_table': 'bebidas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idclien', models.AutoField(db_column='idClien', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellidopat', models.CharField(db_column='apellidoPat', max_length=20)),
                ('apellidomat', models.CharField(db_column='apellidoMat', max_length=20)),
                ('apodo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreprod', models.CharField(db_column='nombreProd', max_length=20)),
                ('cantidadsum', models.IntegerField(db_column='cantidadSum')),
                ('subtotalcom', models.FloatField(db_column='subTotalCom')),
            ],
            options={
                'db_table': 'compras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetallesCompra',
            fields=[
                ('idcom', models.AutoField(db_column='idCom', primary_key=True, serialize=False)),
                ('totalcom', models.FloatField(db_column='totalCom')),
            ],
            options={
                'db_table': 'detalles_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetallesSuministra',
            fields=[
                ('idsum', models.AutoField(db_column='idSum', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'detalles_suministra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('idmem', models.AutoField(db_column='idMem', primary_key=True, serialize=False)),
                ('nombremem', models.CharField(db_column='nombreMem', max_length=20)),
                ('duracion', models.DateField()),
                ('preciomem', models.FloatField(db_column='precioMem')),
            ],
            options={
                'db_table': 'membresia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permanencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('horaentrada', models.TimeField(db_column='horaEntrada')),
                ('horasalida', models.TimeField(db_column='horaSalida')),
            ],
            options={
                'db_table': 'permanencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idprod', models.AutoField(db_column='idProd', primary_key=True, serialize=False)),
                ('nombreprod', models.CharField(db_column='nombreProd', max_length=20)),
                ('stock', models.IntegerField()),
                ('precioprod', models.FloatField(db_column='precioProd')),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idprov', models.AutoField(db_column='idProv', primary_key=True, serialize=False)),
                ('nombreprov', models.CharField(db_column='nombreProv', max_length=20)),
                ('telefono', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('talla', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'ropa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Suministra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreprod', models.CharField(db_column='nombreProd', max_length=20)),
                ('cantidadsum', models.IntegerField(db_column='cantidadSum')),
                ('subtotalsum', models.FloatField(db_column='subTotalSum')),
            ],
            options={
                'db_table': 'suministra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Suplementos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadgramos', models.IntegerField(db_column='cantidadGramos')),
            ],
            options={
                'db_table': 'suplementos',
                'managed': False,
            },
        ),
    ]
