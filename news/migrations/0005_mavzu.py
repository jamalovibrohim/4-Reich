# Generated by Django 5.0 on 2024-01-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_carauthor_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mavzu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100)),
            ],
        ),
    ]