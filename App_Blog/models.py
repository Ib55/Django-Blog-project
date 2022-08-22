from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User,related_name='blog_user',on_delete=models.CASCADE)
    title = models.CharField(max_length=264,verbose_name='Put A Title')
    blog_image = models.ImageField(upload_to='blog_img',verbose_name='Blog Image')
    blog_content = models.TextField(verbose_name='Blog content')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,related_name='comment_user',on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='comment_blog',on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-comment_date']
    def __str__(self):
        return self.comment


class Likes(models.Model):
    user = models.ForeignKey(User,related_name='user_like',on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='like_blog',on_delete=models.CASCADE)
   