# Generated by Django 2.1.5 on 2019-02-17 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0034_mp_mrk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mp_mrk',
            name='item_cd',
        ),
        migrations.RemoveField(
            model_name='mp_mrk',
            name='item_nm',
        ),
    ]
