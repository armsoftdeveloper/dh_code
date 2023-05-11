# Generated by Django 4.2.1 on 2023-05-07 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dh_code', '0024_alter_reviewsru_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advantagesen',
            options={'ordering': ['id'], 'verbose_name': 'Преимущества EN', 'verbose_name_plural': 'Преимущества EN'},
        ),
        migrations.AlterModelOptions(
            name='advantagesru',
            options={'ordering': ['id'], 'verbose_name': 'Преимущества RU', 'verbose_name_plural': 'Преимущества RU'},
        ),
        migrations.AlterModelOptions(
            name='basicen',
            options={'ordering': ['id'], 'verbose_name': 'Главная Страница EN', 'verbose_name_plural': 'Главная Страница EN'},
        ),
        migrations.AlterModelOptions(
            name='basicru',
            options={'ordering': ['id'], 'verbose_name': 'Главная Страница RU', 'verbose_name_plural': 'Главная Страница RU'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['id'], 'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='etapsen',
            options={'ordering': ['id'], 'verbose_name': 'Этапы EN', 'verbose_name_plural': 'Этапы EN'},
        ),
        migrations.AlterModelOptions(
            name='etapsru',
            options={'ordering': ['id'], 'verbose_name': 'Этапы', 'verbose_name_plural': 'Этапы RU'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['id'], 'verbose_name': 'Портфолио', 'verbose_name_plural': 'Портфолио'},
        ),
        migrations.AlterModelOptions(
            name='reviewsen',
            options={'ordering': ['id'], 'verbose_name': 'Отзывы EN', 'verbose_name_plural': 'Отзывы EN'},
        ),
        migrations.AlterModelOptions(
            name='reviewsru',
            options={'ordering': ['id'], 'verbose_name': 'Отзывы RU', 'verbose_name_plural': 'Отзывы RU'},
        ),
        migrations.AlterModelOptions(
            name='servicesen',
            options={'ordering': ['id'], 'verbose_name': 'Услуги EN', 'verbose_name_plural': 'Услуги EN'},
        ),
        migrations.AlterModelOptions(
            name='servicesru',
            options={'ordering': ['id'], 'verbose_name': 'Услуги RU', 'verbose_name_plural': 'Услуги RU'},
        ),
    ]