# Generated by Django 5.1rc1 on 2024-08-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0025_accountlookup_account_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="accountlookup",
            name="follower_type",
            field=models.CharField(choices=[("C", "Celebrity"), ("B", "Best")], default="B", max_length=1),
        ),
    ]
