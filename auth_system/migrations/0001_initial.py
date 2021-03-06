# Generated by Django 4.0.4 on 2022-04-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=3)),
                ('correo_electronico', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('domiciliio', models.CharField(max_length=100)),
                ('cantidad_mascotas', models.CharField(max_length=100)),
                ('razones', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('sexo', models.CharField(blank=True, max_length=100, null=True)),
                ('edad', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_rescate', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='mascotas')),
                ('enfermedades', models.CharField(blank=True, max_length=100, null=True)),
                ('alimentacion', models.CharField(blank=True, max_length=100, null=True)),
                ('adoptante', models.ManyToManyField(blank=True, related_name='mascota', to='auth_system.solicitud')),
            ],
        ),
    ]
