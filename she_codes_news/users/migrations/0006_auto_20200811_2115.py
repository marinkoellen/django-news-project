# Generated by Django 3.0.8 on 2020-08-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200811_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='favourite_cuisine',
            field=models.CharField(choices=[('French', 'French'), ('Italian', 'Italian'), ('Modern Australian', 'Modern Australian'), ('Indonesian', 'Indonesian'), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Thai', 'Thai'), ('American', 'American'), ('Middle Eastern', 'Middle Eastern'), ('Indian', 'Indian'), ('Moroccan', 'Moroccan'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]
