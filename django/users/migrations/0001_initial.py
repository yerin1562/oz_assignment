# Generated by Django 5.1.4 on 2024-12-09 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('age', models.PositiveIntegerField(null=True)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
