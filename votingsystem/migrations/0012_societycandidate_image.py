# Generated by Django 3.2.5 on 2021-07-29 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingsystem', '0011_delete_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='societycandidate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]