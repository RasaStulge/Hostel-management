# Generated by Django 3.2.15 on 2022-08-09 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1, null=True)),
                ('caretaker', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=10)),
                ('room_type', models.CharField(choices=[('S', 'Single Occupancy'), ('F', 'With fridge'), ('FT', 'with fridge and TV')], default=None, max_length=100)),
                ('vacant', models.BooleanField(default=False)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.hostel')),
            ],
        ),
    ]
