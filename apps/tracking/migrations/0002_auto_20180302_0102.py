# Generated by Django 2.0 on 2018-03-02 01:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='behaviourtracking',
            name='friday_arrived',
            field=models.TimeField(blank=True, choices=[(datetime.time(9, 0), datetime.time(9, 0)), (datetime.time(9, 30), datetime.time(9, 30)), (datetime.time(10, 0), datetime.time(10, 0)), (datetime.time(10, 30), datetime.time(10, 30)), (datetime.time(11, 0), datetime.time(11, 0)), (datetime.time(11, 30), datetime.time(11, 30)), (datetime.time(12, 0), datetime.time(12, 0)), (datetime.time(12, 30), datetime.time(12, 30)), (datetime.time(13, 0), datetime.time(13, 0)), (datetime.time(13, 30), datetime.time(13, 30)), (datetime.time(14, 0), datetime.time(14, 0)), (datetime.time(14, 30), datetime.time(14, 30))], default=(datetime.time(9, 0), datetime.time(9, 0))),
        ),
        migrations.AlterField(
            model_name='behaviourtracking',
            name='monday_arrived',
            field=models.TimeField(choices=[(datetime.time(9, 0), datetime.time(9, 0)), (datetime.time(9, 30), datetime.time(9, 30)), (datetime.time(10, 0), datetime.time(10, 0)), (datetime.time(10, 30), datetime.time(10, 30)), (datetime.time(11, 0), datetime.time(11, 0)), (datetime.time(11, 30), datetime.time(11, 30)), (datetime.time(12, 0), datetime.time(12, 0)), (datetime.time(12, 30), datetime.time(12, 30)), (datetime.time(13, 0), datetime.time(13, 0)), (datetime.time(13, 30), datetime.time(13, 30)), (datetime.time(14, 0), datetime.time(14, 0)), (datetime.time(14, 30), datetime.time(14, 30))], default=(datetime.time(9, 0), datetime.time(9, 0))),
        ),
        migrations.AlterField(
            model_name='behaviourtracking',
            name='thursday_arrived',
            field=models.TimeField(blank=True, choices=[(datetime.time(9, 0), datetime.time(9, 0)), (datetime.time(9, 30), datetime.time(9, 30)), (datetime.time(10, 0), datetime.time(10, 0)), (datetime.time(10, 30), datetime.time(10, 30)), (datetime.time(11, 0), datetime.time(11, 0)), (datetime.time(11, 30), datetime.time(11, 30)), (datetime.time(12, 0), datetime.time(12, 0)), (datetime.time(12, 30), datetime.time(12, 30)), (datetime.time(13, 0), datetime.time(13, 0)), (datetime.time(13, 30), datetime.time(13, 30)), (datetime.time(14, 0), datetime.time(14, 0)), (datetime.time(14, 30), datetime.time(14, 30))], default=(datetime.time(9, 0), datetime.time(9, 0))),
        ),
        migrations.AlterField(
            model_name='behaviourtracking',
            name='tuesday_arrived',
            field=models.TimeField(blank=True, choices=[(datetime.time(9, 0), datetime.time(9, 0)), (datetime.time(9, 30), datetime.time(9, 30)), (datetime.time(10, 0), datetime.time(10, 0)), (datetime.time(10, 30), datetime.time(10, 30)), (datetime.time(11, 0), datetime.time(11, 0)), (datetime.time(11, 30), datetime.time(11, 30)), (datetime.time(12, 0), datetime.time(12, 0)), (datetime.time(12, 30), datetime.time(12, 30)), (datetime.time(13, 0), datetime.time(13, 0)), (datetime.time(13, 30), datetime.time(13, 30)), (datetime.time(14, 0), datetime.time(14, 0)), (datetime.time(14, 30), datetime.time(14, 30))], default=(datetime.time(9, 0), datetime.time(9, 0))),
        ),
        migrations.AlterField(
            model_name='behaviourtracking',
            name='wednesday_arrived',
            field=models.TimeField(blank=True, choices=[(datetime.time(9, 0), datetime.time(9, 0)), (datetime.time(9, 30), datetime.time(9, 30)), (datetime.time(10, 0), datetime.time(10, 0)), (datetime.time(10, 30), datetime.time(10, 30)), (datetime.time(11, 0), datetime.time(11, 0)), (datetime.time(11, 30), datetime.time(11, 30)), (datetime.time(12, 0), datetime.time(12, 0)), (datetime.time(12, 30), datetime.time(12, 30)), (datetime.time(13, 0), datetime.time(13, 0)), (datetime.time(13, 30), datetime.time(13, 30)), (datetime.time(14, 0), datetime.time(14, 0)), (datetime.time(14, 30), datetime.time(14, 30))], default=(datetime.time(9, 0), datetime.time(9, 0))),
        ),
    ]
