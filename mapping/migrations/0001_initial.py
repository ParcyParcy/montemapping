# Generated by Django 2.1.2 on 2018-10-30 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField(verbose_name='date published')),
                ('mail_address', models.CharField(max_length=200)),
            ],
        ),
    ]
