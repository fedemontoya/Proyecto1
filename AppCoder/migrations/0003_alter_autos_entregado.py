# Generated by Django 3.2.9 on 2021-12-15 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_auto_20211213_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autos',
            name='entregado',
            field=models.BooleanField(),
        ),
    ]
