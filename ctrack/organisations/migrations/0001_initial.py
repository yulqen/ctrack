# Generated by Django 2.2.9 on 2020-02-20 14:34

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=255)),
                ('line2', models.CharField(blank=True, max_length=255)),
                ('line3', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(blank=True, max_length=100)),
                ('postcode', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
                ('other_details', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name'])),
                ('designation_type', models.IntegerField(choices=[(1, 'Automatic'), (2, 'Reserve Power')], default=1)),
                ('registered_company_name', models.CharField(blank=True, max_length=255)),
                ('registered_company_number', models.CharField(blank=True, max_length=100)),
                ('date_updated', models.DateField(auto_now=True)),
                ('comments', models.TextField(max_length=500)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Submode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(max_length=100)),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisations.Mode')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_nis_contact', models.BooleanField(default=False, verbose_name='Primary NIS contact')),
                ('voluntary_point_of_contact', models.BooleanField(default=False)),
                ('has_egress', models.BooleanField(default=False, verbose_name='Has Egress')),
                ('title', models.IntegerField(choices=[(1, 'Mr'), (2, 'Mrs'), (3, 'Miss'), (4, 'Ms'), (5, 'Dr.'), (6, 'Professor'), (7, 'The Rt Hon.'), (8, 'Lord'), (9, 'Lady')], default=1)),
                ('job_title', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('secondary_email', models.EmailField(blank=True, max_length=254)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('landline', models.CharField(blank=True, max_length=20)),
                ('date_updated', models.DateField(auto_now=True)),
                ('clearance', models.IntegerField(choices=[(1, 'NA'), (2, 'BPSS'), (3, 'CTC'), (4, 'SC'), (5, 'DV'), (6, 'Other')], default=1)),
                ('clearance_sponsor', models.CharField(blank=True, max_length=100)),
                ('clearance_start_date', models.DateField(blank=True, null=True)),
                ('clearance_last_checked', models.DateField(blank=True, null=True)),
                ('clearance_expiry', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('date_ended', models.DateField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, max_length=1000)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisations.Organisation')),
                ('predecessor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='previous_person', to='organisations.Person')),
                ('role', models.ManyToManyField(to='organisations.Role')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
    ]
