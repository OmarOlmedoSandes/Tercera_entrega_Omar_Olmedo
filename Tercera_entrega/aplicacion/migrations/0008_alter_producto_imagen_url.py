# Generated by Django 5.0.2 on 2024-03-12 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_alter_producto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_url',
            field=models.URLField(default='https://dummyimage.com/450x300/dee2e6/6c757d.jpg'),
        ),
    ]
