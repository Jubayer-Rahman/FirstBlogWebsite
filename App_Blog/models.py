from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="What's on your mind?")
    blog_img = models.ImageField(upload_to='blog_images')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return self.blog_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.blog_title)
        super(Blog, self).save(*args, **kwargs)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='blog_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField(verbose_name="Add a comment here...")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    blog = models.ForeignKey(Blog, related_name='liked_blog', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker_user')

    def __str__(self):
        return self.user + "likes" + self.blog
