# Generated by Django 5.1 on 2024-08-11 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=6)),
                ('published_date', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReleaseNote.project')),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseNoteDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=1000, null=True)),
                ('task_size', models.PositiveSmallIntegerField(choices=[(1, 'SMALL'), (2, 'MEDIUM'), (3, 'LARGE')])),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'LOW'), (2, 'MEDIUM'), (3, 'HIGH')])),
                ('task_type', models.PositiveSmallIntegerField(choices=[(1, 'ERROR'), (2, 'FEATURE'), (3, 'IMPROVEMENT')])),
                ('task_domain', models.PositiveSmallIntegerField(choices=[(1, 'SYSTEM'), (2, 'ADMIN'), (3, 'END_USER')])),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('release_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReleaseNote.releasenote')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReleaseNote.user')),
            ],
        ),
    ]
