# Generated by Django 4.2.1 on 2023-05-07 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dh_code', '0023_remove_message_time_create_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewsru',
            options={'ordering': ['-id'], 'verbose_name': 'Отзывы RU', 'verbose_name_plural': 'Отзывы RU'},
        ),
    ]