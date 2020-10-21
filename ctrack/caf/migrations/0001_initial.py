# Generated by Django 3.1.2 on 2020-10-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicableSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='System name assigned by OES', max_length=256)),
                ('function', models.TextField(blank=True, help_text='How the system is relevant to delivering or supporting the essential service', max_length=1000, null=True)),
                ('dft_categorisation', models.CharField(choices=[('CR', 'Critical'), ('IM', 'Important (Legacy use only)')], default='CR', help_text='Refer to documentation for description of these criteria', max_length=2, verbose_name='DfT Categorisation')),
                ('oes_categorisation', models.CharField(default='NA', help_text="Categorisation based on OES' own internal prioritisation process.", max_length=255, verbose_name='OES Categorisation')),
            ],
            options={
                'verbose_name': 'NIS System',
            },
        ),
        migrations.CreateModel(
            name='CAF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(blank=True, max_length=10, null=True)),
                ('triage_review_date', models.DateField(blank=True, null=True)),
                ('comments', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'CAF',
            },
        ),
        migrations.CreateModel(
            name='DocumentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(1, 'Excel'), (2, 'Word'), (3, 'PDF'), (4, 'Hard Copy')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='EssentialService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='FileStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(max_length=100)),
                ('virtual_location', models.CharField(help_text='USB, Rosa, email, etc', max_length=100)),
                ('physical_location', models.CharField(blank=True, help_text='Cupboard, room, building, etc', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(help_text='Q1, C1, etc', max_length=2)),
                ('description', models.TextField(max_length=250)),
                ('type', models.CharField(choices=[('CONFIDENCE', 'Confidence'), ('QUALITY', 'Quality'), ('MISC', 'Misc')], help_text='Type of grading', max_length=20)),
            ],
        ),
    ]
