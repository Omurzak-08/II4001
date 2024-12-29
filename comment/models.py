from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE


class UserProfile(AbstractUser):
    bio = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    website = models.URLField(null=True,blank=True)

    def __str__(self):
        return f'{self.bio}, {self.image} , {self.website}'


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='following',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
     unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower} - {self.following}'


class Post(models.Model):
    user =  models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    image_post = models.ImageField(upload_to='post_images/', null=True , blank=True)
    video_post = models.ImageField(upload_to='post_video/',null=True , blank=True)
    description = models.TextField()
    hashtag = models.CharField(max_length=32, null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} - {self.description} - {self.hashtag}'

class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=CASCADE, related_name='post_like')
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name='like')
    like = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
     unique_together = ('user', 'post')


    def __str__(self):
        return f'{self.user} - {self.post} - {self.like}'


class Comment(models.Model):
    post_comment = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
     unique_together = ('user', 'post_comment')


    def __str__(self):
        return f'{self.post_comment} - {self.user} - {self.text}'

class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comment_likes')
    comment= models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='likes')
    like = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.comment}'

class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='stories')
    image_story = models.ImageField(upload_to='story_images/',null=True, blank=True)
    video_story = models.ImageField(upload_to='story_video')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} - {self.video_story} - {self.image_story} - {self.created_at}'

class Save(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=CASCADE, related_name='saves')

    def __str__(self):
        return f'{self.user}'



class SaveItem(models.Model):
    post =  models.ForeignKey(Post, on_delete=models.CASCADE, related_name='saved_items')
    save = models.ForeignKey(Save, on_delete=models.CASCADE, related_name='items')
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.post}, {self.save}'


class Chat(models.Model):
    person = models.ManyToManyField(UserProfile,)
    created_date = models.DateField(auto_now_add=True)


class Massage(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True  )
    created_date = models.DateField(auto_now_add=True)