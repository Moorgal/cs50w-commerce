# Generated by Django 4.2.3 on 2023-09-22 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_comments_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='listing_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentListing', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
