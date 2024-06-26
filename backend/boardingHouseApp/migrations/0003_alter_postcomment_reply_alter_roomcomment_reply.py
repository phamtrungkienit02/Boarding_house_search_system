# Generated by Django 5.0.4 on 2024-05-14 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardingHouseApp', '0002_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boardingHouseApp.postcomment'),
        ),
        migrations.AlterField(
            model_name='roomcomment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boardingHouseApp.roomcomment'),
        ),
    ]
