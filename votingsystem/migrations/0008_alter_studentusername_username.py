# Generated by Django 3.2.5 on 2021-07-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingsystem', '0007_studentusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentusername',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]