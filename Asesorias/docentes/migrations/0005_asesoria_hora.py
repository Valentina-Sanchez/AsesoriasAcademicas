# Generated by Django 4.2.1 on 2023-06-13 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0004_remove_docente_especializacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asesoria',
            name='hora',
            field=models.TimeField(null=True),
        ),
    ]
