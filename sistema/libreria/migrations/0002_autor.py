# Generated by Django 4.0.5 on 2022-06-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('nacimiento', models.IntegerField(verbose_name='Descripción')),
            ],
        ),
    ]