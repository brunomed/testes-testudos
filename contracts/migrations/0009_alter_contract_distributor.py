# Generated by Django 4.1 on 2023-01-05 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0007_alter_distributor_cnpj_and_more'),
        ('contracts', '0008_alter_contract_distributor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contracts', to='tariffs.distributor'),
            preserve_default=False,
        ),
    ]
