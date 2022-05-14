# Generated by Django 4.0.3 on 2022-05-14 08:14

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('notes', '0004_tagsave_remove_note_htag_alter_category_cate_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tagsave',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '상위 카테고리', 'verbose_name_plural': '상위 카테고리'},
        ),
        migrations.AlterModelOptions(
            name='category2',
            options={'verbose_name': '하위 카테고리', 'verbose_name_plural': '하위 카테고리'},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': '노트', 'verbose_name_plural': '노트'},
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='콤마(,)로 구분합니다.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='태그'),
        ),
    ]