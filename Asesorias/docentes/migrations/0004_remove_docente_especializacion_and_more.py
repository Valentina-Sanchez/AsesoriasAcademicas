# Generated by Django 4.2.1 on 2023-06-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0003_estudiante_email_alter_asesoria_fecha_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docente',
            name='especializacion',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='programa',
        ),
        migrations.AddField(
            model_name='docente',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='docente',
            name='celular',
            field=models.FloatField(max_length=10, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='editado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualización'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='foto',
            field=models.ImageField(upload_to='\\Imágenes\\Django', verbose_name='Foto'),
        ),
        migrations.RemoveField(
            model_name='docente',
            name='materias',
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='editado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualización'),
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='materias',
        ),
        migrations.AlterField(
            model_name='materia',
            name='editado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualización'),
        ),
        migrations.AddField(
            model_name='docente',
            name='materias',
            field=models.ManyToManyField(blank=True, null=True, to='docentes.materia', verbose_name='Materias'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='materias',
            field=models.ManyToManyField(blank=True, null=True, to='docentes.materia', verbose_name='Materias'),
        ),
    ]
