# Generated by Django 2.0.6 on 2018-07-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180717_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userAvatarUrl',
            field=models.URLField(default=''),
        ),
    ]
