# Generated by Django 4.2 on 2023-05-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_alter_userdoc_doc_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdoc',
            name='doc_type',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='userdoc',
            name='docs_image_url',
            field=models.ImageField(upload_to=''),
        ),
    ]