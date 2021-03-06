# Generated by Django 2.1.5 on 2019-02-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0020_delete_mentee'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentee',
            fields=[
                ('mnte_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='멘티ID')),
                ('mnte_nm', models.CharField(max_length=20, verbose_name='멘티 명')),
                ('mnte_nm_e', models.CharField(max_length=20, verbose_name='멘티 영문명')),
                ('brth_dt', models.CharField(max_length=8, verbose_name='생년월일(+ 멘티명 → 동일인 찾기)')),
                ('sch_grd', models.CharField(max_length=1, verbose_name='학교구분')),
                ('sch_cd', models.CharField(max_length=10, verbose_name='학교')),
                ('sch_nm', models.CharField(max_length=30, verbose_name='학교명')),
                ('gen', models.CharField(max_length=1, verbose_name='성별')),
                ('yr', models.CharField(max_length=4, verbose_name='학년도')),
                ('term_div', models.CharField(max_length=2, verbose_name='학기')),
                ('sch_yr', models.CharField(max_length=1, verbose_name='학년')),
                ('mob_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='휴대전화')),
                ('tel_no', models.CharField(blank=True, max_length=12, null=True, verbose_name='집전화')),
                ('grd_id', models.CharField(max_length=10, verbose_name='주 보호자 ID')),
                ('grd_nm', models.CharField(blank=True, max_length=20, null=True, verbose_name='보호자명')),
                ('grd_tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='보호자 연락처')),
                ('grd_rel', models.CharField(blank=True, max_length=2, null=True, verbose_name='보호자 관계(MP0047)')),
                ('prnt_nat_cd', models.CharField(max_length=10, verbose_name='부모출신국가코드')),
                ('prnt_nat_nm', models.CharField(max_length=20, verbose_name='부모출신국가명')),
                ('tchr_id', models.CharField(max_length=10, verbose_name='지도교사 ID')),
                ('tchr_nm', models.CharField(max_length=20, verbose_name='지도교사 명')),
                ('tchr_tel', models.CharField(max_length=20, verbose_name='지도교사 전화번호')),
                ('area_city', models.CharField(max_length=10, verbose_name='시/도')),
                ('area_gu', models.CharField(max_length=10, verbose_name='지역구(시/군)')),
                ('h_addr', models.CharField(max_length=200, verbose_name='집주소')),
                ('h_post_no', models.CharField(blank=True, max_length=6, null=True, verbose_name='우편번호')),
                ('s_addr', models.CharField(max_length=200, verbose_name='학교주소')),
                ('s_post_no', models.CharField(blank=True, max_length=6, null=True, verbose_name='우편번호')),
                ('email_addr', models.CharField(max_length=50, verbose_name='이메일 주소')),
                ('mp_id', models.CharField(max_length=10, verbose_name='첫 지원 멘토링 프로그램ID')),
                ('mp_nm', models.CharField(blank=True, max_length=100, null=True, verbose_name='첫 지원 멘토링 프로그램 명')),
                ('apl_no', models.PositiveIntegerField(verbose_name='첫 지원 멘토링 지원 NO')),
                ('mp_dt', models.CharField(max_length=8, verbose_name='첫 멘토링 시작일')),
                ('cnt_mp_a', models.PositiveIntegerField(default=0, verbose_name='멘토링 지원 경력')),
                ('cnt_mp_p', models.PositiveIntegerField(default=0, verbose_name='멘토링 수행 경력')),
                ('cnt_mp_c', models.PositiveIntegerField(default=0, verbose_name='멘토링 완료 경력')),
                ('cnt_mp_g', models.PositiveIntegerField(default=0, verbose_name='멘토링 중도포기 경력')),
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
