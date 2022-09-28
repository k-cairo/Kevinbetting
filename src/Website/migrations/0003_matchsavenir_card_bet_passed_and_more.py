# Generated by Django 4.1 on 2022-09-28 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_matchsavenir_real_cards_matchsavenir_real_corners'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchsavenir',
            name='card_bet_passed',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='matchsavenir',
            name='corner_bet_passed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='matchsavenir',
            name='real_cards',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matchsavenir',
            name='real_corners',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
