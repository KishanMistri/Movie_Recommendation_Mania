from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160308_1441'),
    ]

    operations = [
        migrations.DeleteModel(
            name='movies',
        ),
    ]
