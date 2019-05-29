# Generated by Django 2.1.7 on 2019-05-21 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20190510_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Department')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='active',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Department'),
        ),
        migrations.AddField(
            model_name='asset',
            name='prepaid_or_postpaid',
            field=models.CharField(blank=True, choices=[('prepaid', 'prepaid'), ('postpaid', 'postpaid')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Department'),
        ),
        migrations.AddField(
            model_name='assetowner',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assetowner',
            name='workspace',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.OfficeWorkspace'),
        ),
        migrations.AddField(
            model_name='asset',
            name='owned_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_by', to='core.AssetOwner'),
        ),
        migrations.RenameField(
            model_name='allocationhistory',
            old_name='current_owner',
            new_name='current_assignee',
        ),
        migrations.RenameField(
            model_name='allocationhistory',
            old_name='previous_owner',
            new_name='previous_assignee',
        ),
    ]