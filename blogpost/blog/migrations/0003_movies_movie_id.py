from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_movies_movieid'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_id',
            field=models.IntegerField(default=0),
        ),
    ]
