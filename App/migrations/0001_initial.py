# Generated by Django 4.0.5 on 2022-06-24 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carerr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.carerr')),
            ],
        ),
    ]
