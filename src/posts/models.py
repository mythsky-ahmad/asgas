from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile


# Create your models here.

class Post(models.Model):
                    # one to many = foregin key
    author = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE) # the post owner
    content = models.TextField()
    image = models.ImageField( upload_to='Posts/', validators = [FileExtensionValidator(['png','jpg','jpeg'])], blank=True, null=True)
    liked = models.ManyToManyField(Profile, blank=True, related_name="Likes") # who liked this post
    updated = models.DateTimeField( auto_now=True, auto_now_add=False)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return str(self.content[:20])

    def num_likes(self):
        return self.liked.all().count()
    #num of commints
    def num_commints(self):
        return self.comments_set.all().count()

    class Meta:
        ordering =('-created',)


class Comment(models.Model):
    user = models.ForeignKey(Profile,  on_delete=models.CASCADE)# the commient owner
    post = models.ForeignKey(Post,  on_delete=models.CASCADE) #  the post owner
    body = models.TextField(max_length=300)
    updated = models.DateTimeField( auto_now=True)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    def __str__(self):
        return str(self.pk)


LIKED_CHOICES= (
    ('Like','Like'),
    ('Unlike','Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(Profile , on_delete=models.CASCADE) # the like owner
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    # the post owner
    value = models.CharField(choices=LIKED_CHOICES, max_length=8)
    updated = models.DateTimeField( auto_now=True)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)        
    def __str__(self):
        return f'{self.user}- to  {self.post.author}-{self.value}'
