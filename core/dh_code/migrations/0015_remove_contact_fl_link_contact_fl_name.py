# Generated by Django 4.2.1 on 2023-05-04 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dh_code', '0014_etaps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='fl_link',
        ),
        migrations.AddField(
            model_name='contact',
            name='fl_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Set Fl Name'),
        ),
    ]