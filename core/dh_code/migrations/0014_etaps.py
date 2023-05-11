# Generated by Django 4.2.1 on 2023-05-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dh_code', '0013_remove_basic_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etaps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=256, verbose_name='Set Page Title')),
                ('title', models.CharField(max_length=256, verbose_name='Set Title')),
                ('description', models.TextField(verbose_name='Set Text')),
                ('actions_title', models.CharField(max_length=256, verbose_name='Set Action Title')),
                ('action_first_title', models.CharField(max_length=256, verbose_name='Set Action First Title')),
                ('action_second_title', models.CharField(max_length=256, verbose_name='Set Action First Title')),
                ('action_third_title', models.CharField(max_length=256, verbose_name='Set Action First Title')),
                ('action_fourth_title', models.CharField(max_length=256, verbose_name='Set Action First Title')),
                ('action_fiveth_title', models.CharField(max_length=256, verbose_name='Set Action First Title')),
            ],
            options={
                'verbose_name': 'Etaps',
                'verbose_name_plural': 'Etaps',
            },
        ),
    ]
