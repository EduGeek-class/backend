# Generated by Django 4.0.3 on 2022-08-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0002_alter_batches_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
