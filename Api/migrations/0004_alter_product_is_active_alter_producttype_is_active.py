# Generated by Django 5.1.6 on 2025-02-16 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_alter_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
