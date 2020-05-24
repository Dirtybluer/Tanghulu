from django.db import models
from users.models import User


# Create your models here.
# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=15, default='someone')
#
#     class Meta:
#         db_table = 'user'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    activity_id = models.IntegerField(default=0)
    content = models.CharField(max_length=100, default='leave something')
    creat_time = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=15)
    # todo:adds user_avatar
    like_num = models.IntegerField(default=0)
    like_user = models.ManyToManyField(User, related_name='comments', through='Comment_like')

    class Meta:
        db_table = 'comment'


class Comment_reply(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replys', default='0')
    from_id = models.IntegerField(default=0)
    from_name = models.CharField(max_length=15, default='someone')
    # todo:adds from_avatar
    to_id = models.IntegerField(default=0)
    to_name = models.CharField(max_length=15, default='someone')
    # todo:adds to_avatar
    content = models.CharField(max_length=100, default='leave something')
    create_time = models.DateTimeField(auto_now_add=True)
    like_num = models.IntegerField(default=0)
    like_user = models.ManyToManyField(User, related_name='comment_replys', through='Comment_reply_like')

    class Meta:
        db_table = 'comment_reply'


class Comment_like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment_like'


class Comment_reply_like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_reply = models.ForeignKey(Comment_reply, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment_reply_like'
