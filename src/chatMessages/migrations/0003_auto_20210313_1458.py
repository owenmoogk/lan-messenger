# Generated by Django 3.1.7 on 2021-03-13 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatMessages', '0002_auto_20210313_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]
