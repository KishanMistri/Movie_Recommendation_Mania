from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='tmdb_id',
            field=models.IntegerField(default=0),
        ),
    ]
