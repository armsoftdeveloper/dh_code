# Generated by Django 4.2.1 on 2023-05-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dh_code', '0011_basic_background_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic',
            name='background_image',
        ),
        migrations.AddField(
            model_name='basic',
            name='video',
            field=models.FileField(null=True, upload_to='video/%Y/%m/%d'),
        ),
    ]