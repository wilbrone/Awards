# Generated by Django 3.0.2 on 2020-02-17 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200217_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile_pics'),
        ),
    ]
