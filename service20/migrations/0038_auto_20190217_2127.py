# Generated by Django 2.1.5 on 2019-02-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0037_auto_20190217_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='mp_mrk',
            name='item_cd',
            field=models.Field(blank=True, null=True, verbose_name='채점항목코드-SEQ별'),
        ),
        migrations.AddField(
            model_name='mp_mrk',
            name='item_nm',
            field=models.Field(blank=True, null=True, verbose_name='채점항목명'),
        ),
    ]
