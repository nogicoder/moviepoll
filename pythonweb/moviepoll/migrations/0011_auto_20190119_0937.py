# Generated by Django 2.1.5 on 2019-01-19 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviepoll', '0010_auto_20190119_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
