# Generated by Django 3.2.19 on 2023-06-22 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_auto_20230621_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencias',
            name='rol',
            field=models.CharField(max_length=20),
        ),
    ]