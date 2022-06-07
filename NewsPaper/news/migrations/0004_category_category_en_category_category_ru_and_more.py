# Generated by Django 4.0.5 on 2022-06-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_category_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_en',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_ru',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
