# Generated by Django 2.0.2 on 2018-11-28 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('behaviour', '0003_merge_20181026_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='behaviourtracking',
            name='friday_arrived',
            field=models.TimeField(blank=True, choices=[(datetime.time(9, 0), '9:00 am'), (datetime.time(9, 30), '9:30 am'), (datetime.time(10, 0), '10:00 am'), (datetime.time(10, 30), '10:30 am'), (datetime.time(11, 0), '11:00 am'), (datetime.time(11, 30), '11:30 am'), (datetime.time(12, 0), '12:00 pm'), (datetime.time(12, 30), '12:30 pm'), (datetime.time(13, 0), '1:00 pm'), (datetime.time(13, 30), '1:30 pm'), (datetime.time(14, 0), '2:00 pm'), (datetime.time(14, 30), '2:30 pm')], default=(datetime.time(9, 0), '9:00 am')),
        ),
        migrations.AlterField(
            model_name='behaviourtracking',
            name='monday_arrived',
            field=models.TimeField(blank=True, choices=[(datetime.time(9, 0), '9:00 am'), (datetime.time(9, 30), '9:30 am'), (datetime.time(10, 0), '10:00 am'), (datetime.time(10, 30), '10:30 am'), (datetime.time(11, 0), '11:00 am'), (datetime.time(11, 30), '11:30 am'), (datetime.time(12, 0), '12:00 pm'), (datetime.time(12, 30), '12:30 pm'), (datetime.time(13, 0), '1:00 pm'), (datetime.time(13, 30), '1:30 pm'), (datetime.time(14, 0), '2:00 pm'), (datetime.time(14, 30), '2:30 pm')], default=(datetime.time(9, 0), '9:00 am')),
        ),
        migrations.AlterField(
            model_name='behaviourtracking',
            name='thursday_arrived',
            field=models.TimeField(blank=True, choices=[(datetime.time(9, 0), '9:00 am'), (datetime.time(9, 30), '9:30 am'), (datetime.time(10, 0), '10:00 am'), (datetime.time(10, 30), '10:30 am'), (datetime.time(11, 0), '11:00 am'), (datetime.time(11, 30), '11:30 am'), (datetime.time(12, 0), '12:00 pm'), (datetime.time(12, 30), '12:30 pm'), (datetime.time(13, 0), '1:00 pm'), (datetime.time(13, 30), '1:30 pm'), (datetime.time(14, 0), '2:00 pm'), (datetime.time(14, 30), '2:30 pm')], default=(datetime.time(9, 0), '9:00 am')),
        ),
        migrations.AlterField(
            model_name='behaviourtracking',
            name='tuesday_arrived',
            field=models.TimeField(blank=True, choices=[(datetime.time(9, 0), '9:00 am'), (datetime.time(9, 30), '9:30 am'), (datetime.time(10, 0), '10:00 am'), (datetime.time(10, 30), '10:30 am'), (datetime.time(11, 0), '11:00 am'), (datetime.time(11, 30), '11:30 am'), (datetime.time(12, 0), '12:00 pm'), (datetime.time(12, 30), '12:30 pm'), (datetime.time(13, 0), '1:00 pm'), (datetime.time(13, 30), '1:30 pm'), (datetime.time(14, 0), '2:00 pm'), (datetime.time(14, 30), '2:30 pm')], default=(datetime.time(9, 0), '9:00 am')),
        ),
        migrations.AlterField(
            model_name='behaviourtracking',
            name='wednesday_arrived',
            field=models.TimeField(blank=True, choices=[(datetime.time(9, 0), '9:00 am'), (datetime.time(9, 30), '9:30 am'), (datetime.time(10, 0), '10:00 am'), (datetime.time(10, 30), '10:30 am'), (datetime.time(11, 0), '11:00 am'), (datetime.time(11, 30), '11:30 am'), (datetime.time(12, 0), '12:00 pm'), (datetime.time(12, 30), '12:30 pm'), (datetime.time(13, 0), '1:00 pm'), (datetime.time(13, 30), '1:30 pm'), (datetime.time(14, 0), '2:00 pm'), (datetime.time(14, 30), '2:30 pm')], default=(datetime.time(9, 0), '9:00 am')),
        ),
    ]
