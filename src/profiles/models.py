from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField( max_length=100 , blank=True )
    last_name = models.CharField( max_length=100 , blank=True )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='No Bio...' , max_length=300)
    email = models.EmailField(blank=True ,  max_length=254)
    country = models.CharField( max_length=100 , blank=True )
    avatar = models.ImageField(upload_to='avatars/'  , default = 'avatar.png' )
    friends = models.ManyToManyField(User, blank=True ,  related_name='friends')
    slug = models.SlugField(unique= True , blank= True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    #post // author = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE) # the post owner
    #commint // user = models.ForeignKey(Profile,  on_delete=models.CASCADE)# the commient owner    
    #like // user = models.ForeignKey(Profile, on_delete=models.CASCADE) # the like owner
    def get_friends(self):
        return self.friends.all()

    def get_friends_num(self):
        return self.friends.all().count()

    def get_posts_num(self):
        return self.posts.all().count() # return self.post_set.all() coz the related name
    def get_all_authors_posts(self):
        return self.posts.all() 

    def get_likes_given_num(self):
        likes = self.like_set.all() # self.likes.all() if the realated name="likes" in Like model
        total_liked = 0
        for item in likes:
            if item.value == "Like":
                total_liked += 1
        return total_liked
    
    def get_likes_received_num(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts :
            total_liked += item.liked.all().count()
        return total_liked

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"


    def save(self , *args, **kwargs):

        ex = False
        if self.last_name and self.first_name:
            to_slug = slugify(str(self.first_name) +" "+str(self.last_name))
            ex = Profile.objects.filter(slug=to_slug).exists()
            while ex :
                to_slug = slugify(to_slug+" "+ str(get_random_code()))
                ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
            
        self.slug = to_slug
        super(Profile,self).save(*args,**kwargs) 


class Relationship(models.Model):
    STATUS_CHOICES = (
        ("send","send"),
        ("accepted" , "accepted")
    )
    sender = models.ForeignKey(Profile , on_delete=models.CASCADE , related_name="sender")
    receiver = models.ForeignKey(Profile , on_delete=models.CASCADE , related_name="reseiver")
    status = models.CharField(choices=STATUS_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"

    def __unicode__(self):
        return 
