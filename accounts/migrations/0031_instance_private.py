# Generated by Django 5.1.5 on 2025-01-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0030_auto_20241201_1217"),
    ]

    operations = [
        migrations.AddField(
            model_name="instance",
            name="private",
            field=models.BooleanField(default=False),
        ),
    ]
