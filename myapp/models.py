# from _typeshed import Self
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from autoslug import AutoSlugField

# Create your models here.
class Post(models.Model):   
    post_id = models.AutoField
    post_title = models.CharField(max_length=100, default="")
    post_desc = models.CharField(max_length=5000, default="")
    post_category = models.IntegerField(choices=[(1,"Computer Science"),(2,"Mechanical"),(3,"Civil"),(4,"Electronics"),(5,"MBA"),(6,"BBA")])
    post_likes = models.ManyToManyField(User,blank=True,related_name='likes')
    post_dislikes = models.ManyToManyField(User,blank=True,related_name='dislikes')
    post_user =models.ForeignKey(User, on_delete= models.CASCADE)
    slug = AutoSlugField(populate_from='post_title',unique=True,null=True,default=None)
    post_date = models.DateField(auto_now=True)
    post_images = models.ImageField(upload_to="myapp/images", default="",null=True)    

    def __str__(self):
        return self.post_title
    
    def total_likes(self):
        return self.post_likes.count()

class postComment(models.Model):
    sno = models.AutoField(primary_key= True)
    comment = models.TextField()    
    user =models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null= True)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13]+"..."+" by "+ self.user.username
