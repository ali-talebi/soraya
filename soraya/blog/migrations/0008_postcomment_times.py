# Generated by Django 5.1 on 2024-08-24 06:48

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_postcomment_post_selected_alter_post_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="postcomment",
            name="times",
            field=django_jalali.db.models.jDateTimeField(
                auto_now_add=True, null=True, verbose_name=""
            ),
        ),
    ]
