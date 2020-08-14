# Generated by Django 2.2.12 on 2020-08-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caf', '0006_auto_20200813_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicablesystem',
            name='oes_categorisation',
            field=models.CharField(default='', help_text="Categorisation based on OES' own internal prioritisation process.", max_length=255, verbose_name='OES Categorisation'),
        ),
        migrations.AlterField(
            model_name='applicablesystem',
            name='dft_categorisation',
            field=models.CharField(choices=[('CR', 'Critical'), ('IM', 'Important (Legacy use only)')], default='CR', help_text='Refer to documentation for description of these criteria', max_length=2, verbose_name='DfT Categorisation'),
        ),
    ]