# Generated by Django 5.0.6 on 2024-06-29 18:08

import Library_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library_app', '0003_alter_libro_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='precio',
            field=models.IntegerField(default=Library_app.models.precio_random),
        ),
    ]