# Generated by Django 3.2 on 2021-05-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_auto_20210503_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisecomment',
            name='content',
            field=models.TextField(default='', null=True),
        ),
    ]