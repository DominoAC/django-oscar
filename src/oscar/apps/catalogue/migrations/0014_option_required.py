# Generated by Django 2.1 on 2019-03-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_auto_20170821_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='required',
            field=models.BooleanField(default=False, verbose_name='Is option required?'),
        ),
    ]