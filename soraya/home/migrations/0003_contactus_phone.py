# Generated by Django 5.1 on 2024-08-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_contactus"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactus",
            name="phone",
            field=models.CharField(max_length=11, null=True, verbose_name="شماره تلفن"),
        ),
    ]
