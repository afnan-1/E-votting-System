# Generated by Django 3.2.5 on 2021-07-28 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votingsystem', '0003_auto_20210728_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='societycandidate',
            name='team',
        ),
        migrations.AddField(
            model_name='societycandidate',
            name='society',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='society', to='votingsystem.societie'),
            preserve_default=False,
        ),
    ]
