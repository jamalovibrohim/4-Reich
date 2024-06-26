# Generated by Django 5.0 on 2024-01-19 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_mavzu'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Masala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharti', models.TextField()),
                ('mavzu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mavzu_masala', to='news.mavzu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_masala', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
