# Generated by Django 4.0.3 on 2022-04-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Do not show', 'Do not show'), ('Male', 'Male'), ('Female', 'Female')], default='Do not show', max_length=11, null=True),
        ),
    ]
