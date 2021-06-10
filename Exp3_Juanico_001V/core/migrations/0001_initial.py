# Generated by Django 3.2.3 on 2021-06-10 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Usuario')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('cargo', models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='Cargo Admin')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]
