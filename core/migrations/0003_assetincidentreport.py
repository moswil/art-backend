# Generated by Django 2.0.1 on 2018-05-23 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_auto_20180515_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetIncidentReport',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_type', models.CharField(
                    choices=[('Loss', 'Loss'),
                             ('Damage', 'Damage')], max_length=50)),
                ('incident_location', models.CharField(max_length=50)),
                ('incident_description', models.CharField(max_length=255)),
                ('injuries_sustained', models.CharField(max_length=50)),
                ('loss_of_property', models.CharField(max_length=50)),
                ('witnesses', models.CharField(max_length=50)),
                ('police_abstract_obtained',
                 models.BooleanField(default=False)),
                ('asset', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    to='core.Asset',
                    to_field='serial_number')),
            ],
        ),
    ]