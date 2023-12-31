# Generated by Django 4.2.5 on 2023-09-28 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chats", "0007_remove_userprofilemodel_user_delete_chatnotification_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Thread",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "thread_type",
                    models.CharField(
                        choices=[("personal", "Personal"), ("group", "Group")],
                        default="group",
                        max_length=15,
                    ),
                ),
                ("users", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("text", models.TextField()),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "thread",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="chats.thread"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
