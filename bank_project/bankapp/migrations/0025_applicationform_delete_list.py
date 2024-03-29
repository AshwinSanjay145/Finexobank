# Generated by Django 4.2.9 on 2024-01-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0024_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='applicationform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('acctype', models.CharField(max_length=255)),
                ('materials', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='list',
        ),
    ]
