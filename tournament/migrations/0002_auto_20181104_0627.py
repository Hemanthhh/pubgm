# Generated by Django 2.1.2 on 2018-11-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='paytm',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='pubg_uid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='whatsapp',
            field=models.IntegerField(),
        ),
    ]