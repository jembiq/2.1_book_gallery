# Generated by Django 4.1.1 on 2022-09-11 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
