# Generated by Django 2.0.1 on 2023-10-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
            ],
        ),
    ]
