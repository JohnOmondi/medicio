# Generated by Django 3.2.12 on 2024-07-15 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runserver', '0007_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
