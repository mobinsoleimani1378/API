# Generated by Django 4.2.7 on 2023-12-02 09:47

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
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email address')),
                ('fullname', models.CharField(max_length=50, verbose_name='نام کامل')),
                ('phone', models.CharField(max_length=12, null=True, unique=True, verbose_name='phone number')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False, verbose_name='ادمین')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('code', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
            ],
        ),
    ]
