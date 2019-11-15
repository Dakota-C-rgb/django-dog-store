# Generated by Django 2.2.5 on 2019-11-15 18:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20191115_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogtag',
            name='dog_color',
            field=models.TextField(default=datetime.datetime(2019, 11, 15, 18, 55, 4, 692842, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchased_at',
            field=models.DateField(verbose_name=datetime.datetime(2019, 11, 15, 18, 54, 40, 374344)),
        ),
    ]
