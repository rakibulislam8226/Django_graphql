# Generated by Django 4.1 on 2022-11-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postCreate', '0002_alter_extenduser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]