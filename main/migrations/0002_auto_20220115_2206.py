# Generated by Django 3.2.7 on 2022-01-16 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_num', models.FloatField(default=113.4938)),
                ('lat_num', models.FloatField(default=53.5461)),
                ('num', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Latitude',
        ),
        migrations.DeleteModel(
            name='Longitude',
        ),
        migrations.DeleteModel(
            name='Passenger',
        ),
    ]