# Generated by Django 3.1.2 on 2020-10-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_auto_20201030_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='code',
            field=models.CharField(max_length=30, null=True, verbose_name='証券コード'),
        ),
    ]
