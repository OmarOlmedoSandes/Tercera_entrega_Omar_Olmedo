# Generated by Django 5.0.2 on 2024-03-11 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_alter_producto_imagen_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=80),
        ),
    ]
