# Generated by Django 3.2.5 on 2021-07-28 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votingsystem', '0005_auto_20210728_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='societycandidate',
            name='voter',
        ),
    ]
