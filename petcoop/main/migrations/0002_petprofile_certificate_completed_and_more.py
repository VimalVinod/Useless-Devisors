# Generated by Django 4.2.4 on 2024-11-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petprofile',
            name='certificate_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='petprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='petprofile',
            name='interests',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='petprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
