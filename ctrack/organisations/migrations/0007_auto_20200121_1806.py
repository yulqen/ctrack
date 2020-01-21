# Generated by Django 2.2.9 on 2020-01-21 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0006_auto_20200121_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='organisations.Organisation'),
        ),
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisations.AddressType'),
        ),
    ]
