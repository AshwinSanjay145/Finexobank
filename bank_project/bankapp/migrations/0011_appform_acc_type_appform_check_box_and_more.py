# Generated by Django 4.2.9 on 2024-01-17 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0010_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appform',
            name='acc_type',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appform',
            name='check_box',
            field=models.BooleanField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appform',
            name='credit_card',
            field=models.BooleanField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appform',
            name='debit_card',
            field=models.BooleanField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appform',
            name='passbook',
            field=models.BooleanField(default='1'),
            preserve_default=False,
        ),
    ]
