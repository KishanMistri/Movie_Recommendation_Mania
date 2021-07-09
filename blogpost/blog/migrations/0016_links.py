from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160310_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=300)),
            ],
        ),
    ]
