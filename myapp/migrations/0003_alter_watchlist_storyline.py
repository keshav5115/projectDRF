# Generated by Django 4.2.6 on 2023-10-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_review_watchlist_alter_watchlist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='storyline',
            field=models.CharField(max_length=200),
        ),
    ]
