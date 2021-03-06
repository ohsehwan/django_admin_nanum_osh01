# Generated by Django 2.1.5 on 2019-02-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0012_cm_surv_a'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cm_cnv_scr',
            options={},
        ),
        migrations.AlterField(
            model_name='cm_cnv_scr',
            name='eval_item',
            field=models.CharField(max_length=2, verbose_name='항목(MS0023)'),
        ),
        migrations.AlterField(
            model_name='cm_cnv_scr',
            name='ins_dt',
            field=models.DateField(blank=True, null=True, verbose_name='입력일시'),
        ),
        migrations.AlterField(
            model_name='cm_cnv_scr',
            name='upd_dt',
            field=models.DateField(blank=True, null=True, verbose_name='수정일시'),
        ),
        migrations.AlterUniqueTogether(
            name='cm_cnv_scr',
            unique_together=set(),
        ),
    ]
