# Generated by Django 4.0.5 on 2022-06-10 10:50

import coomon.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_created_book_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('birth_year', models.IntegerField()),
                ('death_year', models.IntegerField(blank=True, null=True)),
                ('bioream', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, coomon.models.CheckAgeMixin),
        ),
    ]
