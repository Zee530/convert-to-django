# Generated by Django 5.1.5 on 2025-02-12 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sophia', '0003_contactform_phone_alter_contactform_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='Contactquery',
        ),
    ]
