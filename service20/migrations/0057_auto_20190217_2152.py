# Generated by Django 2.1.5 on 2019-02-17 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0056_auto_20190217_2152'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mp_mte',
            unique_together={('mp_id', 'mnte_no')},
        ),
    ]
