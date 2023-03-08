# Generated by Django 3.2.17 on 2023-02-02 09:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crawler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField(blank=True, help_text='프로젝트가 keyword 모드일 경우 수집할 검색어 목록(쉼표로 구분), tag 모드일 경우 빈칸', verbose_name='KEYWORD')),
                ('state', models.CharField(choices=[('Initialized', 'Initialized'), ('Running', 'Running'), ('Done', 'Done'), ('Stopped', 'Stopped')], default='Running', help_text='크롤러의 동작 상태 (iniialized/ running/ done/ stopped)', max_length=20, verbose_name='STATE')),
                ('collected', models.IntegerField(default=0, help_text='수집한 이미지/단어 개수', verbose_name='COLLECTED')),
                ('create_dt', models.DateTimeField(auto_now_add=True, help_text='크롤러 생성 날짜', verbose_name='CREATE DT')),
                ('website', models.CharField(choices=[('https://www.farfetch.com/kr/shopping/women/search/items.aspx', 'farfetch-women(keyword)'), ('https://www.farfetch.com/kr/shopping/men/search/items.aspx', 'farfetch-men(keyword)'), ('https://www.farfetch.com/kr/shopping/women/clothing-1/items.aspx', 'farfetch-women(tag)'), ('https://www.farfetch.com/kr/shopping/men/clothing-2/items.aspx', 'farfetch-men(tag)')], help_text='크롤러가 수집하는 웹사이트 url', max_length=200, verbose_name='WEBSITE')),
                ('pid', models.IntegerField(default=-1, help_text='크롤러 실행 중인 프로세스 ID', verbose_name='PID')),
                ('elapsed', models.DurationField(default=datetime.timedelta(0), help_text='크롤러 생성 후 경과 시간', verbose_name='ELAPSED TIME')),
                ('remaining', models.DurationField(default=datetime.timedelta(0), help_text='크롤러 실행 완료까지 남은 예상 시간', verbose_name='REMAINING TIME')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='생성할 프로젝트의 이름', max_length=100, unique=True, verbose_name='NAME')),
                ('mode', models.CharField(choices=[('Keyword', 'Keyword'), ('Tag', 'Tag')], help_text='생성할 프로젝트의 모드 (keyword/tag)', max_length=20, verbose_name='MODE')),
                ('state', models.CharField(choices=[('Initialized', 'Initialized'), ('Running', 'Running'), ('Done', 'Done'), ('Stopped', 'Stopped')], default='Initialized', help_text='프로젝트 진행 상태 (initialized/ running/ done/ stopped)', max_length=20, verbose_name='STATE')),
                ('collected', models.IntegerField(default=0, help_text='수집한 이미지/단어 개수', verbose_name='COLLECTED')),
                ('create_dt', models.DateTimeField(auto_now_add=True, help_text='프로젝트 생성 날짜', verbose_name='CREATE DT')),
                ('elapsed', models.DurationField(default=datetime.timedelta(0), help_text='프로젝트 생성 후 경과 시간', verbose_name='ELAPSED TIME')),
                ('remaining', models.DurationField(blank=True, default=datetime.timedelta(0), help_text='프로젝트 실행 완료까지 남은 예상 시간', verbose_name='REMAINING TIME')),
            ],
            options={
                'ordering': ('create_dt',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', jsonfield.fields.JSONField(blank=True, default=dict, verbose_name='TAG')),
                ('crawler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.crawler')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.project')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(help_text='이미지 원본 url', verbose_name='URL')),
                ('save_path', models.TextField(default='/', help_text='이미지가 저장되어 있는 path', verbose_name='SAVE PATH')),
                ('cut', models.CharField(blank=True, choices=[('Unfiltered', 'Unfiltered'), ('Outfit', 'Outfit'), ('Dummy', 'Dummy'), ('Product', 'Product'), ('Detail', 'Detail'), ('Etc', 'Etc')], default='Unfiltered', help_text='Outfit, Dummy, Product, Detail, Etc 중 택1', max_length=20, verbose_name='CUT')),
                ('part', models.CharField(blank=True, choices=[('Unfiltered', 'Unfiltered'), ('Full', 'Full'), ('Top', 'Top'), ('Bottom', 'Bottom')], default='Unfiltered', help_text='Full, Top, Bottom 중 택1', max_length=20, verbose_name='PART')),
                ('direction', models.CharField(blank=True, choices=[('Unfiltered', 'Unfiltered'), ('Front', 'Front'), ('Left_45', 'Left_45'), ('Left', 'Left'), ('Back', 'Back'), ('Right', 'Right'), ('Right_45', 'Right_45')], default='Unfiltered', help_text='Front, Left_45, Left, Back, Right, Right_45 항목 중 택1', max_length=20, verbose_name='DIRECTION')),
                ('pose', models.CharField(blank=True, choices=[('Unfiltered', 'Unfiltered'), ('Stand', 'Stand'), ('Sit_in_chair', 'Sit_in_chair'), ('Sit_in_floor', 'Sit_in_floor'), ('Etc', 'Etc')], default='Unfiltered', help_text='Stand, Sit_in_chair, Sit_in_floor, Etc 중 택1', max_length=20, verbose_name='POSE')),
                ('is_head', models.CharField(blank=True, choices=[('Unfiltered', 'Unfiltered'), ('Is_head', 'Is_head'), ('Not_head', 'Not_head')], default='Unfiltered', help_text='Head, Not_head 중 택1', max_length=20, verbose_name='IS HEAD')),
                ('person_count', models.CharField(blank=True, choices=[('Unfiltered', 'Unfiltered'), ('One', 'One'), ('Two_more', 'Two_more')], default='Unfiltered', help_text='One, Two_more 중 택1', max_length=20, verbose_name='PERSON COUNT')),
                ('crawler', models.ForeignKey(help_text='해당 이미지가 수집된 크롤러의 키값', on_delete=django.db.models.deletion.CASCADE, to='crawler.crawler')),
                ('project', models.ForeignKey(help_text='해당 이미지가 수집된 프로젝트의 키값', on_delete=django.db.models.deletion.CASCADE, to='crawler.project')),
            ],
        ),
        migrations.AddField(
            model_name='crawler',
            name='project',
            field=models.ForeignKey(help_text='해당 크롤러가 할당되어있는 프로젝트의 키값', on_delete=django.db.models.deletion.CASCADE, to='crawler.project'),
        ),
    ]
