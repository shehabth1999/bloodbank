# Generated by Django 5.0.6 on 2024-06-22 09:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_donationrequest_is_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
