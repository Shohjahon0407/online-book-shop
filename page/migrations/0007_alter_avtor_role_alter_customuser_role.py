# Generated by Django 5.2.3 on 2025-06-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avtor',
            name='role',
            field=models.CharField(choices=[('Admin', 'admin'), ('Reader', 'reader'), ('Publisher', 'publisher')], default='Reader', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'admin'), ('Reader', 'reader'), ('Publisher', 'publisher')], default='Reader', max_length=20),
        ),
    ]
