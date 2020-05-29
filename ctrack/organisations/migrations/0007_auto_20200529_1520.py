# Generated by Django 2.2.12 on 2020-05-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0006_incidentreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentreport',
            name='dft_handle_status',
            field=models.CharField(choices=[('queued', 'QUEUED'), ('reviewing', 'REVIEWING'), ('waiting', 'WAITING'), ('completed', 'COMPLETE')], default='queued', max_length=20),
        ),
        migrations.AlterField(
            model_name='incidentreport',
            name='date_time_incident_reported',
            field=models.DateTimeField(auto_now=True, verbose_name='Date/Time incident reported'),
        ),
    ]