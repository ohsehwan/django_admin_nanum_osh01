# Generated by Django 2.1.5 on 2019-02-17 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0064_auto_20190217_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cm_cnv_scr',
            options={'verbose_name': '점수변환표', 'verbose_name_plural': '점수변환표'},
        ),
        migrations.AlterUniqueTogether(
            name='cm_cnv_scr',
            unique_together={('eval_item', 'eval_seq')},
        ),
    ]
