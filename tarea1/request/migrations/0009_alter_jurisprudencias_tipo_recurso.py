# Generated by Django 3.2.19 on 2023-06-22 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0008_auto_20230621_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencias',
            name='tipo_recurso',
            field=models.CharField(max_length=100),
        ),
    ]
