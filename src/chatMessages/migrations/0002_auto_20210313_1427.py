# Generated by Django 3.1.7 on 2021-03-13 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatMessages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='description',
            new_name='text',
        ),
    ]