# Generated by Django 4.2.6 on 2023-10-31 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_place_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='place_db',
            name='Description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
