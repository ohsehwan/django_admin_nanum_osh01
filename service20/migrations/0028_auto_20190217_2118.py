# Generated by Django 2.1.5 on 2019-02-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0027_auto_20190217_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mp_mrk',
            name='test_div',
            field=models.CharField(max_length=10, verbose_name='전형구분(서류/면접)MP0039'),
        ),
    ]