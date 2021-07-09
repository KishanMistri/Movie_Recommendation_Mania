from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0011_auto_20160310_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(default=0)),
                ('imdb_id', models.IntegerField()),
                ('tmdb_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(default=0)),
                ('imdb_id', models.IntegerField(default=0)),
                ('movie_name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('vectors', models.CharField(max_length=20)),
            ],
        ),
    ]
