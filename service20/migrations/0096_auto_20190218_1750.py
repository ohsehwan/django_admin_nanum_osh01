# Generated by Django 2.1.5 on 2019-02-18 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service20', '0095_delete_ms_sub'),
    ]

    operations = [
        migrations.CreateModel(
            name='ms_sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ms_id', models.CharField(max_length=10, verbose_name='멘토스쿨ID')),
                ('att_id', models.CharField(max_length=10, verbose_name='속성ID')),
                ('att_seq', models.PositiveIntegerField(verbose_name='속성 SEQ → PK 자동생성 시 필요없음')),
                ('att_cdh', models.CharField(blank=True, max_length=6, null=True, verbose_name='속성 CODE HEADER')),
                ('att_cdd', models.CharField(blank=True, max_length=10, null=True, verbose_name='속성 CODE')),
                ('att_val', models.CharField(blank=True, max_length=60, null=True, verbose_name='속성 값')),
                ('att_unit', models.CharField(blank=True, max_length=10, null=True, verbose_name='속성 단위')),
                ('use_yn', models.CharField(blank=True, max_length=1, null=True, verbose_name='사용여부')),
                ('sort_seq', models.PositiveIntegerField(default=1, verbose_name='정렬')),
                ('ins_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='입력자ID')),
                ('ins_ip', models.CharField(blank=True, max_length=20, null=True, verbose_name='입력자IP')),
                ('ins_dt', models.DateTimeField(blank=True, null=True, verbose_name='입력일시')),
                ('ins_pgm', models.CharField(blank=True, max_length=20, null=True, verbose_name='입력프로그램ID')),
                ('upd_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='수정자ID')),
                ('upd_ip', models.CharField(blank=True, max_length=20, null=True, verbose_name='수정자IP')),
                ('upd_dt', models.DateTimeField(blank=True, null=True, verbose_name='수정일시')),
                ('upd_pgm', models.CharField(blank=True, max_length=20, null=True, verbose_name='수정프로그램ID')),
            ],
            options={
                'verbose_name': '개설멘토스쿨 속성(질문지, 채점항목,채점자)',
                'verbose_name_plural': '개설멘토스쿨 속성(질문지, 채점항목,채점자)',
            },
        ),
        migrations.AlterUniqueTogether(
            name='ms_sub',
            unique_together={('ms_id', 'att_id', 'att_seq')},
        ),
    ]
