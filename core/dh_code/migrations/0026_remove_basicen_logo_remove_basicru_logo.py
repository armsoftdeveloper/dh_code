# Generated by Django 4.2.1 on 2023-05-07 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dh_code', '0025_alter_advantagesen_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicen',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='basicru',
            name='logo',
        ),
    ]
