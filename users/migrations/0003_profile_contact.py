# Generated by Django 4.1.1 on 2022-11-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_profiles_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
