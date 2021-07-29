# Generated by Django 3.2.5 on 2021-07-29 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(blank=True, choices=[('CS', 'CS'), ('BBA', 'BBA'), ('HND', 'HND'), ('BTECH', 'BTECH')], max_length=10, null=True),
        ),
    ]
