# Generated by Django 5.0.6 on 2024-06-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library_app', '0002_delete_carrito_libro_precio_alter_libro_imagen_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='precio',
            field=models.IntegerField(default=5000),
        ),
    ]
