# Generated by Django 3.2 on 2021-05-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0002_alter_exercise_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='contest_type',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='contest',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='contest',
            name='status',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='input',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='output',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='exercisecomment',
            name='content',
            field=models.TextField(default=''),
        ),
    ]