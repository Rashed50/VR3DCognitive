# Generated by Django 4.2.16 on 2024-11-20 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
                'db_table': 'country',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VRModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sessionID', models.CharField(max_length=150)),
                ('frame_number', models.CharField(max_length=20)),
                ('timestamp', models.CharField(max_length=150)),
                ('sensor_data', models.TextField(max_length=500)),
            ],
            options={
                'db_table': 'vr3d_info',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='VRUser',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vr_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_no', models.CharField(blank=True, max_length=13, null=True)),
                ('state_id', models.SmallIntegerField(default=1)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, max_length=300, null=True)),
                ('address2', models.TextField(blank=True, max_length=300, null=True)),
                ('zip', models.CharField(blank=True, max_length=10, null=True)),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DataSource.country')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'vrusers',
                'ordering': ['-created_at'],
            },
        ),
    ]
