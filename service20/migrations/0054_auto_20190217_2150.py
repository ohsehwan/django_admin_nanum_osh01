# Generated by Django 2.1.5 on 2019-02-17 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0053_auto_20190217_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mp_mte',
            options={'verbose_name': '프로그램 지원자(멘티)', 'verbose_name_plural': '프로그램 지원자(멘티)'},
        ),
        migrations.AlterUniqueTogether(
            name='mp_mte',
            unique_together={('mp_id', 'mnte_no')},
        ),
    ]
