# Generated by Django 3.0.6 on 2020-05-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_auto_20200517_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lemonadeproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]