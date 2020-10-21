# Generated by Django 3.1.2 on 2020-10-21 15:51

import ctrack.organisations.models
from django.conf import settings
import django.contrib.auth
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='deputy_lead_inspector',
            field=models.ForeignKey(null=True, on_delete=models.SET(ctrack.organisations.models.Organisation.get_sentinel_user), related_name='deputy_inspector', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organisation',
            name='lead_inspector',
            field=models.ForeignKey(null=True, on_delete=models.SET(ctrack.organisations.models.Organisation.get_sentinel_user), related_name='lead_inspector', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organisation',
            name='submode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisations.submode'),
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisations.organisation'),
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='reporting_person',
            field=models.ForeignKey(on_delete=models.SET(django.contrib.auth.get_user_model), to='organisations.person', verbose_name='Person reporting the incident'),
        ),
        migrations.AddField(
            model_name='address',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='organisations.organisation'),
        ),
        migrations.AddField(
            model_name='address',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisations.addresstype', verbose_name='Address Type'),
        ),
    ]
