# Generated by Django 3.1.1 on 2020-09-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_service_time_needed'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default='<django.db.models.fields.CharField>'),
        ),
    ]