# Generated by Django 3.0.6 on 2020-05-17 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20200516_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='commission',
        ),
    ]