# Generated by Django 3.0.8 on 2020-08-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200802_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_upload',
            field=models.URLField(blank=True, default='', max_length=500, null=True),
        ),
    ]
