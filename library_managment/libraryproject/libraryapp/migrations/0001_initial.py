# Generated by Django 3.2 on 2022-06-09 07:46

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('emailid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'admin',
            },
            managers=[
                ('Objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Authorname', models.CharField(blank=True, max_length=50, null=True)),
                ('bookprice', models.CharField(blank=True, max_length=50, null=True)),
                ('booklocation', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'book',
            },
            managers=[
                ('Objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
