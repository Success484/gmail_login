# Generated by Django 5.0.3 on 2024-12-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlepass',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]