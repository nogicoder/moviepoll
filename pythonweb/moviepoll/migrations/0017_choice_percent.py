# Generated by Django 2.1.5 on 2019-01-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviepoll', '0016_auto_20190119_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='percent',
            field=models.IntegerField(default=0),
        ),
    ]
