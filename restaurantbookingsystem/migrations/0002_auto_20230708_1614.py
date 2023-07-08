# Generated by Django 3.2.19 on 2023-07-08 16:14

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurantbookingsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_email', models.EmailField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date', 'start_time'],
            },
        ),
        migrations.CreateModel(
            name='BookingQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='table',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='table',
            name='table_number',
        ),
        migrations.AddField(
            model_name='table',
            name='code',
            field=models.CharField(default='', max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='image',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255, verbose_name='table_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='capacity',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.AddField(
            model_name='booking',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantbookingsystem.table'),
        ),
    ]
