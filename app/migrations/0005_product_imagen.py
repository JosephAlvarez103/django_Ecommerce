# Generated by Django 5.0.4 on 2024-04-24 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_impuesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
