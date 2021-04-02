# Generated by Django 3.1.7 on 2021-04-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='state',
            field=models.CharField(choices=[('P', 'pending'), ('A', 'accepted'), ('R', 'rejected')], default='P', max_length=1, null=True),
        ),
    ]
