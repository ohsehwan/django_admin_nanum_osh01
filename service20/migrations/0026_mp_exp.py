# Generated by Django 2.1.5 on 2019-02-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0025_mp_rep'),
    ]

    operations = [
        migrations.CreateModel(
            name='mp_exp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mp_id', models.CharField(max_length=10, verbose_name='멘토링 프로그램ID')),
                ('apl_no', models.PositiveIntegerField(verbose_name='멘토 지원 NO')),
                ('exp_no', models.PositiveIntegerField(verbose_name='활동비 NO')),
                ('exp_mon', models.CharField(max_length=6, verbose_name='활동비 월')),
                ('exp_div', models.CharField(max_length=1, verbose_name='활동비 구분')),
                ('exp_ttl', models.CharField(blank=True, max_length=200, null=True, verbose_name='활동비 제목')),
                ('exp_dt', models.DateTimeField(blank=True, null=True, verbose_name='활동비 작성일')),
                ('bank_dt', models.DateTimeField(blank=True, null=True, verbose_name='은행 자료 작성일')),
                ('elap_tm', models.TimeField(blank=True, null=True, verbose_name='활동시간 합계')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='시급(단가)')),
                ('appr_tm', models.PositiveIntegerField(blank=True, null=True, verbose_name='인정시간 합계')),
                ('sum_exp', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='활동비=APPR_TM * UNIT_PRICE')),
                ('bank_acct', models.CharField(blank=True, max_length=20, null=True, verbose_name='은행 계좌 번호')),
                ('bank_cd', models.CharField(blank=True, max_length=10, null=True, verbose_name='은행 코드')),
                ('bank_nm', models.CharField(blank=True, max_length=50, null=True, verbose_name='은행 명')),
                ('bank_dpsr', models.CharField(blank=True, max_length=20, null=True, verbose_name='예금주')),
                ('mp_sname', models.CharField(blank=True, max_length=20, null=True, verbose_name='입금자명-멘토링 프로그램 단명')),
                ('mgr_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='관리자ID')),
                ('mgr_dt', models.DateTimeField(blank=True, null=True, verbose_name='관리자 승인일시')),
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
