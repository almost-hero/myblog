# Generated by Django 2.2.1 on 2019-05-29 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190528_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(blank=True, max_length=150, unique=True),
        ),
    ]
