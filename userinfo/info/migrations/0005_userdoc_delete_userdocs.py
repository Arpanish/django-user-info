# Generated by Django 4.2 on 2023-05-10 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_userdocs'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bbox', models.CharField(max_length=15)),
                ('docs_image_url', models.URLField()),
                ('doc_type', models.CharField(max_length=55)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserDocs',
        ),
    ]
