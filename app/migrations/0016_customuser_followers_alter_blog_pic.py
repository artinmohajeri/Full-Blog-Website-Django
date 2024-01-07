# Generated by Django 5.0 on 2024-01-07 06:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='user_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pic',
            field=models.ImageField(blank=True, default='blog_pictures/img-1.jpg', null=True, upload_to='blog_pictures/'),
        ),
    ]
