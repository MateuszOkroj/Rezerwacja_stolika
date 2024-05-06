# Generated by Django 5.0.3 on 2024-04-11 18:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stolik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc', models.PositiveSmallIntegerField()),
                ('restauracja', models.CharField(choices=[('BISTRO', 'bistro'), ('CHIŃCZYK', 'chińczyk'), ('MEKSYKAŃSKA', 'meksykańska'), ('PIZZA WŁOSKA', 'pizza włoska'), ('RAMENOWNIA', 'ramenownia')], default='BISTRO', max_length=16)),
                ('nakrycie', models.CharField(choices=[('Tak', 'tak'), ('Nie', 'nie')], default='TAK', max_length=16)),
                ('lokalizacja', models.CharField(choices=[('PRZY OKNIE', 'przy oknie'), ('PRZY BARZE', 'przy barze'), ('NA ŚRODKU', 'na środku')], default='NA ŚRODKU', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Rezerwacja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('stolik', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Rezerwacje.stolik')),
            ],
        ),
    ]