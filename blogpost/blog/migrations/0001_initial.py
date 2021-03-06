from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieID', models.IntegerField(unique=True)),
                ('movie_name', models.CharField(max_length=100, unique=True)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
