# Generated by Django 3.1.2 on 2020-10-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_urlshortenerurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortenerurl',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]