# Generated by Django 3.0.8 on 2020-10-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RasioKeuangan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_bank', models.CharField(max_length=150)),
                ('tahun', models.CharField(max_length=10)),
                ('car', models.DecimalField(decimal_places=4, max_digits=19)),
                ('npl', models.DecimalField(decimal_places=4, max_digits=19)),
                ('roa', models.DecimalField(decimal_places=4, max_digits=19)),
                ('roe', models.DecimalField(decimal_places=4, max_digits=19)),
                ('nim', models.DecimalField(decimal_places=4, max_digits=19)),
                ('ldr', models.DecimalField(decimal_places=4, max_digits=19)),
            ],
            options={
                'db_table': 'data_rasio_keuangan',
            },
        ),
    ]
