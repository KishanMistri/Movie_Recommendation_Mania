from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_meansize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meansize',
            name='movie_id',
            field=models.IntegerField(default=0),
        ),
    ]
