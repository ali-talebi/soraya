# Generated by Django 5.1 on 2024-08-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_post_author_idea"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="banner1",
            field=models.FileField(
                null=True,
                upload_to="Post/Banner/banner1",
                verbose_name="بنر تبلیغاتی 1 ",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="banner2",
            field=models.FileField(
                null=True,
                upload_to="Post/Banner/banner2",
                verbose_name="بنر تبلیغاتی 2 ",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="banner3",
            field=models.FileField(
                null=True,
                upload_to="Post/Banner/banner3",
                verbose_name="بنر تبلیغاتی  3",
            ),
        ),
    ]
