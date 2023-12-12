# Generated by Django 4.1 on 2022-11-28 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0005_distributor_is_active'),
        ('contracts', '0007_contract_distributor_alter_contract_tariff_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='distributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contracts', to='tariffs.distributor'),
        ),
    ]
