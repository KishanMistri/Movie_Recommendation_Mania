from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_delete_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='meansize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.FloatField(default=0.0)),
                ('mean', models.FloatField(default=0.0)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.movies')),
            ],
        ),
    ]
