from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_movies_movie_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='movies',
        ),
    ]
