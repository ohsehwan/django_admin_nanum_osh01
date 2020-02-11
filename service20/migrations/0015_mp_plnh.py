# Generated by Django 2.1.5 on 2019-02-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0014_cm_sms'),
    ]

    operations = [
        migrations.CreateModel(
            name='mp_plnh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mp_id', models.CharField(max_length=10, verbose_name='멘토링 프로그램ID')),
                ('apl_no', models.PositiveIntegerField(verbose_name='멘토 지원 NO')),
                ('pln_weeks', models.PositiveIntegerField(verbose_name='계획 주차 수')),
                ('mtr_obj', models.CharField(blank=True, max_length=1000, null=True, verbose_name='학습목표')),
                ('pln_dt', models.DateTimeField(blank=True, null=True, verbose_name='계획작성일')),
                ('req_dt', models.DateTimeField(blank=True, null=True, verbose_name='승인요청일')),
                ('appr_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='승인자ID')),
                ('appr_nm', models.CharField(blank=True, max_length=20, null=True, verbose_name='승인자명')),
                ('appr_dt', models.DateTimeField(blank=True, null=True, verbose_name='보호자 승인일시')),
                ('mgr_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='관리자ID')),
                ('mgr_dt', models.DateTimeField(blank=True, null=True, verbose_name='관리자 승인일시')),
                ('status', models.CharField(blank=True, max_length=2, null=True, verbose_name='상태')),
                ('ins_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='입력자ID')),
                ('ins_ip', models.CharField(blank=True, max_length=20, null=True, verbose_name='입력자IP')),
                ('ins_dt', models.DateTimeField(blank=True, null=True, verbose_name='입력일시')),
                ('ins_pgm', models.CharField(blank=True, max_length=20, null=True, verbose_name='입력프로그램ID')),
                ('upd_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='수정자ID')),
                ('upd_ip', models.CharField(blank=True, max_length=20, null=True, verbose_name='수정자IP')),
                ('upd_dt', models.DateTimeField(blank=True, null=True, verbose_name='수정일시')),
                ('upd_pgm', models.CharField(blank=True, max_length=20, null=True, verbose_name='수정프로그램ID')),
            ],
        ),
    ]