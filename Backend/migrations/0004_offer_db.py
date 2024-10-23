# Generated by Django 4.2.6 on 2023-11-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_place_db_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(blank=True, max_length=30, null=True)),
                ('Place', models.CharField(blank=True, max_length=30, null=True)),
                ('Details', models.CharField(blank=True, max_length=30, null=True)),
                ('Rating', models.CharField(blank=True, max_length=30, null=True)),
                ('Hotel', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('Discount', models.IntegerField(blank=True, null=True)),
                ('Image1', models.ImageField(blank=True, null=True, upload_to='offers')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='offers')),
                ('Image3', models.ImageField(blank=True, null=True, upload_to='offers')),
                ('Image4', models.ImageField(blank=True, null=True, upload_to='offers')),
            ],
        ),
    ]
