# Generated by Django 2.0.1 on 2018-05-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180529_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetincidentreport',
            name='injuries_sustained',
            field=models.TextField(blank=True, null=True),
        ),
    ]
