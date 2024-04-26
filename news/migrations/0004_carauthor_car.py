# Generated by Django 5.0 on 2024-01-10 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_author_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_a', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rusumi', models.CharField(max_length=20)),
                ('yili', models.CharField(max_length=10)),
                ('ca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auto', to='news.carauthor')),
            ],
        ),
    ]
