# Generated by Django 3.2.19 on 2023-07-08 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantbookingsystem.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100)),
                ('guest_email', models.EmailField(max_length=254)),
                ('reservation_date', models.DateField()),
                ('reservation_time', models.TimeField()),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantbookingsystem.table')),
            ],
        ),
    ]
