# Generated by Django 5.0.4 on 2024-05-07 20:42

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_product_imagen'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendedorGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
