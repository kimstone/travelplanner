# Generated by Django 2.2 on 2021-05-01 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucketlist',
            name='location',
        ),
    ]
