# Generated by Django 2.1.2 on 2018-10-30 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='reg_date',
        ),
    ]