# Generated by Django 5.0.6 on 2024-06-19 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_donationrequest_delete_donationrequest2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DonationRequest',
        ),
    ]
