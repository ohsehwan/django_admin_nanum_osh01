# Generated by Django 2.1.5 on 2019-02-17 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0066_auto_20190217_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mp_plnh',
            options={'verbose_name': '프로그램 수행 계획서', 'verbose_name_plural': '프로그램 수행 계획서'},
        ),
        migrations.AlterUniqueTogether(
            name='mp_plnh',
            unique_together={('mp_id', 'apl_no')},
        ),
        migrations.AlterIndexTogether(
            name='mp_plnh',
            index_together={('apl_no',)},
        ),
    ]
