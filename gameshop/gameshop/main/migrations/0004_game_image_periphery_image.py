# Generated by Django 4.0.3 on 2022-04-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_game_date_of_release_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='periphery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
