# Generated by Django 4.2 on 2023-05-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_userdoc_delete_userdocs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdoc',
            name='doc_type',
            field=models.ImageField(upload_to=''),
        ),
    ]
