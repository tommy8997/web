# Generated by Django 2.0.3 on 2018-03-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_bounties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalbounty',
            name='action_url',
            field=models.URLField(db_index=True, default='https://gitcoin.co'),
            preserve_default=False,
        ),
    ]
