# Generated by Django 2.1.5 on 2019-01-17 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviepoll', '0003_auto_20190117_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='moviepoll.Question'),
        ),
    ]
