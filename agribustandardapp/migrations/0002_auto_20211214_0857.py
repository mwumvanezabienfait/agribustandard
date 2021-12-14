# Generated by Django 3.2.9 on 2021-12-14 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agribustandardapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idafarmuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessiondId', models.CharField(max_length=255, null=True)),
                ('serviceCode', models.CharField(max_length=255, null=True)),
                ('phoneNumber', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('sizeOfland', models.CharField(max_length=255)),
                ('names', models.CharField(max_length=255)),
                ('idnumber', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Crop',
        ),
    ]
