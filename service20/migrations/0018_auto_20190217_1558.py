# Generated by Django 2.1.5 on 2019-02-17 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0017_auto_20190217_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='sch_yr',
        ),
        migrations.RemoveField(
            model_name='mentee',
            name='term_div',
        ),
        migrations.RemoveField(
            model_name='mentee',
            name='yr',
        ),
    ]
