# Generated by Django 4.0.5 on 2023-08-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('serialCarroseria', models.CharField(max_length=50)),
                ('serialMotor', models.CharField(max_length=50)),
                ('tags', models.CharField(choices=[['Particular', 'Particular'], ['Transporte', 'Transporte'], ['Carga', 'Carga']], default='Particular', max_length=20)),
                ('precio', models.CharField(max_length=256)),
            ],
        ),
    ]