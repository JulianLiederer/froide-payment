# Generated by Django 2.1.7 on 2019-03-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('froide_payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_donation',
            field=models.BooleanField(default=False),
        ),
    ]
