# Generated by Django 4.2.1 on 2023-06-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0002_alter_asesoria_docente_alter_asesoria_estudiante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='asesoria',
            name='fecha',
            field=models.DateField(verbose_name='Fecha de Asesoria'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='celular',
            field=models.FloatField(max_length=10, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='foto',
            field=models.ImageField(upload_to='\\Imágenes\\Django', verbose_name='Foto'),
        ),
    ]
