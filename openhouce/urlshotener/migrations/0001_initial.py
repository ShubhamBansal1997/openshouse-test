# Generated by Django 3.0.7 on 2020-08-26 14:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('url', models.TextField()),
                ('shorten_url_code', models.TextField()),
            ],
            options={
                'verbose_name': 'ShortURL',
                'verbose_name_plural': 'ShortURLs',
                'ordering': ['-created_at'],
            },
        ),
    ]
