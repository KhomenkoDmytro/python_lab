# Generated by Django 4.1.7 on 2023-04-26 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
    ]
