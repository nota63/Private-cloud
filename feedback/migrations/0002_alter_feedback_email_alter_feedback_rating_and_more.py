# Generated by Django 5.0.6 on 2024-07-08 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='recommend',
            field=models.CharField(max_length=3),
        ),
    ]