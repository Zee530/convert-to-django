# Generated by Django 5.1.5 on 2025-02-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sophia', '0002_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
