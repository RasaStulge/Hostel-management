# Generated by Django 3.2.15 on 2022-08-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('S', 'Single Occupancy'), ('F', 'With fridge'), ('FT', 'with fridge and TV')], default=None, max_length=10000),
        ),
    ]
