# Generated by Django 4.1.2 on 2022-10-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('created_by', models.CharField(max_length=20)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
