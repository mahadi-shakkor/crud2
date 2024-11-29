# Generated by Django 5.1.3 on 2024-11-29 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apP', '0002_user_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vid', models.OneToOneField(db_column='VID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='apP.user')),
            ],
            options={
                'db_table': 'vendor',
                'managed': False,
            },
        ),
    ]
