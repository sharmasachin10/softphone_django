# Generated by Django 2.0.10 on 2019-11-13 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Softphone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client_name', models.CharField(default='', max_length=20, null=True)),
                ('client_id', models.CharField(default='', max_length=20, null=True)),
                ('switch_id', models.CharField(default='', max_length=20, null=True)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(default='', max_length=1000, null=True)),
                ('client', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Softphone.Clients')),
            ],
            options={
                'db_table': 'instructions',
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('compay_address', models.CharField(default='', max_length=200, null=True)),
                ('location_type', models.CharField(default='', max_length=20, null=True)),
                ('timezone', models.CharField(default='', max_length=30, null=True)),
                ('client', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Softphone.Clients')),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(default='', max_length=50, null=True)),
                ('last_name', models.CharField(default='', max_length=50, null=True)),
                ('email', models.CharField(default='', max_length=70, null=True)),
                ('phone', models.CharField(default='', max_length=20, null=True)),
                ('client', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Softphone.Clients')),
                ('location', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Softphone.Locations')),
            ],
            options={
                'db_table': 'personnel',
            },
        ),
        migrations.CreateModel(
            name='WorkHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_day', models.CharField(default='', max_length=200, null=True)),
                ('end_day', models.CharField(default='', max_length=20, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('client', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Softphone.Clients')),
                ('location', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Softphone.Locations')),
            ],
            options={
                'db_table': 'workhours',
            },
        ),
        migrations.AddField(
            model_name='instructions',
            name='location',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Softphone.Locations'),
        ),
    ]
