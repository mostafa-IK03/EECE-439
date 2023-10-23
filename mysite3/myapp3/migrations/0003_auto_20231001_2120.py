# Generated by Django 2.0.1 on 2023-10-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0002_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='address',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='author',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='reason',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='title',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
