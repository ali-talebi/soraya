# Generated by Django 5.1 on 2024-08-24 07:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_postcomment_times"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="author_idea",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="نظر نویسنده"),
        ),
    ]
