from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_movies'),
    ]

    operations = [
        migrations.DeleteModel(
            name='links',
        ),
        migrations.DeleteModel(
            name='movies',
        ),
    ]
