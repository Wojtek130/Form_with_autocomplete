# Generated by Django 4.0.1 on 2022-01-16 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('password_conf', models.CharField(max_length=100)),
                ('birth_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
