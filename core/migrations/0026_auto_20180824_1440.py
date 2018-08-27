# Generated by Django 2.0.1 on 2018-08-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20180824_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetstatus',
            name='current_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Allocated', 'Allocated'), ('Lost', 'Lost'), ('Damaged', 'Damaged')], default='Available', max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='asset',
            unique_together={('asset_code', 'serial_number')},
        ),
    ]
