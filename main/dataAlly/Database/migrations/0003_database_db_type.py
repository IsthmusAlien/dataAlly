# Generated by Django 4.2.1 on 2024-05-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Database", "0002_database_db_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="database",
            name="db_type",
            field=models.CharField(default="", max_length=100),
        ),
    ]
