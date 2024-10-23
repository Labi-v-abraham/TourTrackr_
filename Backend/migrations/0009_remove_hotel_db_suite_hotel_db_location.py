# Generated by Django 4.2.6 on 2023-11-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0008_hotel_db'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel_db',
            name='Suite',
        ),
        migrations.AddField(
            model_name='hotel_db',
            name='Location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
