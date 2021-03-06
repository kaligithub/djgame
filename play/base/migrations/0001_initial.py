# Generated by Django 3.1.7 on 2021-03-12 05:03

from django.db import migrations, models
import play.base.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('api_key', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('api_secret_key', models.CharField(default=play.base.models.get_random_string_value, editable=False, max_length=32)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'API Keys',
                'verbose_name_plural': 'API Keys',
            },
        ),
    ]
