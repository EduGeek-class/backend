# Generated by Django 5.0.3 on 2024-03-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0006_alter_profile_batch_codes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studymaterial',
            name='batch_code',
            field=models.IntegerField(default=2201, max_length=4),
        ),
    ]
