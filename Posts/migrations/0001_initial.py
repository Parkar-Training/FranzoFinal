# Generated by Django 3.2 on 2021-11-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('PostId', models.AutoField(primary_key=True, serialize=False)),
                ('PuserId', models.IntegerField(error_messages={'required': 'enter user id'})),
                ('Post_Time', models.DateTimeField(auto_now=True)),
                ('Like_count', models.IntegerField(blank=True, default=0)),
                ('Post_data', models.CharField(error_messages={'required': 'Post content cannot be blank'}, max_length=80)),
            ],
        ),
    ]