# Generated by Django 3.0 on 2022-04-29 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20220428_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Pokemon')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='parties',
            field=models.ManyToManyField(related_name='parties', through='blog.Party', to=settings.AUTH_USER_MODEL),
        ),
    ]