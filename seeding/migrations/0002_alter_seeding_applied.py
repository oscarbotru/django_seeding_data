# Generated by Django 4.0.4 on 2022-05-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeding',
            name='applied',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Applied date'),
        ),
    ]
