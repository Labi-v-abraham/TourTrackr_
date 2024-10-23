# Generated by Django 4.2.6 on 2023-11-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelBooking_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotel_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('First_Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Email_Id', models.CharField(blank=True, max_length=80, null=True)),
                ('Room', models.CharField(blank=True, max_length=50, null=True)),
                ('No_of_people', models.IntegerField(blank=True, null=True)),
                ('Arrive_Date', models.CharField(blank=True, max_length=50, null=True)),
                ('Arrive_Time', models.CharField(blank=True, max_length=50, null=True)),
                ('Time', models.CharField(blank=True, max_length=20, null=True)),
                ('Departure_Month', models.CharField(blank=True, max_length=30, null=True)),
                ('Departure_Day', models.CharField(blank=True, max_length=30, null=True)),
                ('Departure_Year', models.CharField(blank=True, max_length=30, null=True)),
                ('Pick_Up', models.CharField(blank=True, max_length=40, null=True)),
                ('Flight_No', models.CharField(blank=True, max_length=100, null=True)),
                ('Request', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]