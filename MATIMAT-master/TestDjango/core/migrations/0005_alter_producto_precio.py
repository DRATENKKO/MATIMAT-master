# Generated by Django 4.0.4 on 2022-06-04 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_producto_imagen_alter_producto_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.CharField(max_length=9),
        ),
    ]
