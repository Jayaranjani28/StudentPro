# Generated by Django 4.0.1 on 2022-01-10 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_studentinfo_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
