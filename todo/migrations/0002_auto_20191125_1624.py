# Generated by Django 2.2.7 on 2019-11-25 10:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivedtask',
            name='complete_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 10, 54, 1, 181374, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='completedtask',
            name='complete_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 10, 54, 1, 181374, tzinfo=utc)),
        ),
    ]
