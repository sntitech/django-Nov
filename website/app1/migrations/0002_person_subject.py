# Generated by Django 4.2.7 on 2023-11-17 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='subject',
            field=models.CharField(default='', max_length=200),
        ),
    ]