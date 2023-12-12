# Generated by Django 4.2.7 on 2023-12-08 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phonenumber', models.BigIntegerField()),
                ('designation', models.CharField(max_length=50)),
                ('teacherid', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='rollnumber',
            field=models.IntegerField(default=0),
        ),
    ]