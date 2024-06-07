# Generated by Django 5.0.6 on 2024-06-07 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='geo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.geo'),
        ),
    ]
