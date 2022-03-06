# Generated by Django 4.0.2 on 2022-03-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbti', models.CharField(db_column='mbti', max_length=50)),
                ('user_name', models.CharField(db_column='user_name', max_length=100)),
                ('content_text', models.TextField(db_column='content_text', max_length=255)),
                ('like_count', models.IntegerField(db_column='like_count')),
                ('tag_list', models.CharField(db_column='tag_list', max_length=250)),
            ],
            options={
                'db_table': 't_insta_data',
                'managed': False,
            },
        ),
    ]
