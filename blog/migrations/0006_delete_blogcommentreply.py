# Generated by Django 3.2.11 on 2022-01-21 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogcommentreply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogCommentReply',
        ),
    ]
