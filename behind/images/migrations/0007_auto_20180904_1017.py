# Generated by Django 2.0.6 on 2018-09-04 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_auto_20180903_1702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_at']},
        ),
    ]