# Generated by Django 2.1 on 2018-08-29 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrolled',
            field=models.BooleanField(default=True),
        ),
    ]