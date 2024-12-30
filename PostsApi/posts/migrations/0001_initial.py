# Generated by Django 5.1.4 on 2024-12-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_id', models.IntegerField(blank=True, null=True)),
                ('post_parent_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField()),
                ('posts_content', models.TextField()),
                ('posts_created_on', models.DateTimeField(auto_now_add=True)),
                ('posts_created_by', models.CharField(max_length=45)),
                ('posts_modified_on', models.DateTimeField(auto_now=True)),
                ('posts_modified_by', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
    ]
