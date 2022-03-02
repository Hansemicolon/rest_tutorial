from django.db import models

# Create your models here.

class board(models.Model):
    mbti = models.CharField(db_column='mbti', max_length=50)
    user_name = models.CharField(db_column='user_name', max_length=100)
    content_text = models.TextField(db_column='content_text', max_length=255)
    like_count = models.IntegerField(db_column='like_count',)
    # short_code = models.CharField(db_column='shord_code', max_length=250)
    # media_id = models.CharField(db_column='media_id', max_length=250)
    # published_at = models.DateTimeField(db_column='published_at', )
    tag_list = models.CharField(db_column='tag_list', max_length=250)
    # user_id = models.CharField(db_column='user_id', max_length=250)

    class Meta:
        managed = False
        db_table = 't_insta_crawler'
