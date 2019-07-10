# Generated by Django 2.1 on 2019-07-09 13:32

import core.models.asset
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_assetincidentreport_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetincidentreport',
            name='police_abstract',
            field=models.FileField(blank=True, upload_to=core.models.asset.user_abstract, verbose_name='Police Abstract'),
        ),
    ]
