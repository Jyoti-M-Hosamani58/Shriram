# Generated by Django 5.0.6 on 2024-09-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0002_remove_addconsignment_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='track_number',
            field=models.CharField(max_length=50),
        ),
    ]