# Generated by Django 2.1.5 on 2019-02-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0018_auto_20190217_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='yr',
            field=models.CharField(default=2, max_length=4, verbose_name='학년도'),
            preserve_default=False,
        ),
    ]
