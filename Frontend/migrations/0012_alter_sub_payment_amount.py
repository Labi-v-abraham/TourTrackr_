# Generated by Django 4.2.6 on 2023-12-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0011_alter_sub_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_payment',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
