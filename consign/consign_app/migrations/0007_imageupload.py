# Generated by Django 5.0.6 on 2024-09-30 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0006_enquiry_userlogin_vehicle_emission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
